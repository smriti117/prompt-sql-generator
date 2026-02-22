from fastapi import APIRouter, WebSocket, WebSocketDisconnect
from app.services.query_executor import QueryExecutor
from app.services.sql_validator import SQLValidator
from app.services.lru_cache import LRUCache
import asyncio

from app.services.llm.factory import get_llm

# Initializing services
router = APIRouter()
executor = QueryExecutor()
validator = SQLValidator()
lru_cache = LRUCache(capacity=50)
llm = get_llm()


@router.websocket("/ws/query")
async def websocket_query(websocket: WebSocket):
    await websocket.accept()

    try:
        while True:
            user_prompt = await websocket.receive_text()
            await websocket.send_json({"stage": "generating_sql"})

            try:
                generated_sql = await llm.generate_sql(user_prompt)
                await websocket.send_json(
                    {"stage": "generated_sql", "sql": generated_sql}
                )

                valid, message = validator.validate(generated_sql)
                if not valid:
                    await websocket.send_json({"stage": "error", "message": message})
                    continue

                cached = lru_cache.get(generated_sql)
                if cached:
                    await websocket.send_json({"stage": "cache_hit", "result": cached})
                    continue

                await websocket.send_json({"stage": "executing"})
                result = await executor.execute(generated_sql)

                lru_cache.put(generated_sql, result)
                await websocket.send_json({"stage": "done", "result": result})

            except Exception as e:
                print(f"Error processing query: {e}")
                await websocket.send_json(
                    {"stage": "error", "message": f"Processing error: {str(e)}"}
                )

    except WebSocketDisconnect:
        print("Client disconnected")
    except Exception as e:
        print(f"WebSocket connection error: {e}")

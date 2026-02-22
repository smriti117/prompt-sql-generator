from fastapi import FastAPI
from app.db.session import engine, Base
from app.db import models
from app.api.websocket import router as ws_router


# Initialize FASTAPI
app = FastAPI()


app.include_router(ws_router)


# # STARTUP DB
# @app.on_event("startup")
# async def startup():
#     async with engine.begin() as conn:
#         await conn.run_sync(Base.metadata.create_all)


@app.get("/")
async def health():
    return {"status": "ok"}

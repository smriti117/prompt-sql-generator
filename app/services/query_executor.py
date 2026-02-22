from sqlalchemy import text
from app.db.session import AsyncSessionLocal


class QueryExecutor:
    async def execute(self, sql_query: str):
        async with AsyncSessionLocal() as session:
            result = await session.execute(text(sql_query))
            rows = result.mappings().all()
            return [dict(row) for row in rows]

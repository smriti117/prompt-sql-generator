import asyncio
from app.services.llm.base import BaseLLMService


class MockLLMService(BaseLLMService):
    async def generate_sql(self, prompt: str) -> str:
        await asyncio.sleep(1)  # simulate AI latency

        prompt_lower = prompt.lower()

        if "all users" in prompt_lower:
            return "SELECT * FROM users LIMIT 10"

        if "count users" in prompt_lower:
            return "SELECT COUNT(*) FROM users"

        return "SELECT * FROM users LIMIT 5"

class BaseLLMService:
    async def generate_sql(self, prompt: str) -> str:
        raise NotImplementedError

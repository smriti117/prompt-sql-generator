import asyncio
from openai import AsyncOpenAI
from app.services.llm.base import BaseLLMService
from config.settings import env


class OpenAILLMService(BaseLLMService):
    def __init__(self):
        self.api_key = env.llm_provider_key
        self.model = env.provider_model or "gpt-4o-mini"
        self.client = AsyncOpenAI(api_key=self.api_key)

    async def generate_sql(self, prompt: str) -> str:
        system_prompt = """
You are a SQL generator.
Only return a valid PostgreSQL SELECT query.
Do not explain anything.
Do not return text other than SQL.
        """

        try:
            response = await asyncio.wait_for(
                self.client.chat.completions.create(
                    model=self.model,
                    messages=[
                        {"role": "system", "content": system_prompt},
                        {"role": "user", "content": prompt},
                    ],
                    temperature=0,
                ),
                timeout=10,
            )

            sql = response.choices[0].message.content.strip()
            return sql

        except asyncio.TimeoutError:
            print("OpenAI timeout")
            return "SELECT 1"
        except Exception as e:
            print(f"OpenAI error: {e}")
            return "SELECT 1"

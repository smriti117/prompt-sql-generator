import os
import httpx
from app.services.llm.base import BaseLLMService
from config.settings import env


class OllamaLLMService(BaseLLMService):
    def __init__(self):
        # Using default values if specific OLLAMA_URL is not provided (should be in env)
        self.base_url = os.getenv("OLLAMA_URL", "http://localhost:11434")
        self.model = env.provider_model

    async def generate_sql(self, prompt: str) -> str:
        print(f"Using Ollama LLM with model: {self.model}")

        system_prompt = """
                    You are a senior PostgreSQL query generator.
                    Convert natural language questions into SAFE PostgreSQL SELECT queries.
                    Table: users (id, name, email)
                    Rules:
                    1. ONLY SELECT statements.
                    2. LIMIT 50.
                    3. No explanations, no markdown.
                    """

        try:
            async with httpx.AsyncClient() as client:
                response = await client.post(
                    f"{self.base_url}/api/generate",
                    json={
                        "model": self.model,
                        "prompt": f"{system_prompt}\nUser: {prompt}",
                        "stream": False,
                    },
                    timeout=15.0,  # Shorter timeout for better UX
                )
                response.raise_for_status()
                data = response.json()
                return data.get("response", "SELECT 1;").strip()
        except (httpx.TimeoutException, httpx.RequestError) as e:
            print(f"Ollama LLM error: {e}")
            return "SELECT 1; # Fallback due to LLM timeout"
        except Exception as e:
            print(f"Unexpected LLM error: {e}")
            return "SELECT 1;"

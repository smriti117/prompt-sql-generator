from app.services.llm.mock import MockLLMService
from app.services.llm.openai_service import OpenAILLMService
from app.services.llm.ollama_service import OllamaLLMService
import os
from config.settings import env


def get_llm():
    provider = env.llm_provider

    if provider == "openai":
        return OpenAILLMService()

    if provider == "ollama":
        return OllamaLLMService()

    return MockLLMService()

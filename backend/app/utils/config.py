# app/utils/config.py
from pydantic_settings import BaseSettings
from functools import lru_cache
from enum import Enum

class SummarizerProvider(str, Enum):
    OPENAI = "openai"
    ANTHROPIC = "anthropic"
    LOCAL = "local"

    @classmethod
    def default(cls) -> "SummarizerProvider":
        return cls.OPENAI

class PromptVersion(str, Enum):
    V1 = "v1"
    V2 = "v2"
    # Add new versions as needed

    @classmethod
    def latest(cls) -> "PromptVersion":
        return cls.V1

class Settings(BaseSettings):
    # Google OAuth
    google_client_id: str
    google_client_secret: str
    
    # Email
    email_account: str
    
    # Database
    mongo_uri: str
    
    # Environment
    environment: str = "development"

    # AI Providers
    openai_api_key: str
    deepseek_api_key: str | None = None
    gemini_api_key: str | None = None
    
    # Summarizer settings
    summarizer_provider: SummarizerProvider = SummarizerProvider.default()
    summarizer_model: str = "gpt-4o-mini" # TODO enum that maps providers to models
    summarizer_batch_threshold: int = 10
    summarizer_prompt_version: PromptVersion = PromptVersion.latest()
    
    class Config:
        env_file = ".env"
        use_enum_values = True
        
@lru_cache()
def get_settings() -> Settings:
    return Settings()
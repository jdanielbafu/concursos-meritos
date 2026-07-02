from pydantic_settings import BaseSettings
from typing import List

class Settings(BaseSettings):
    DATABASE_URL: str = ""
    SUPABASE_JWT_SECRET: str = ""
    ALLOWED_ORIGINS: List[str] = ["http://localhost:3000"]
    DEBUG: bool = True

    class Config:
        env_file = ".env"

    def __init__(self, **values):
        super().__init__(**values)
        self.DATABASE_URL = self.DATABASE_URL.strip()

# Instancia global — importa esto desde otros archivos
settings = Settings()
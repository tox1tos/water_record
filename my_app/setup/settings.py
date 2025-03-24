from pydantic_settings import BaseSettings

class AppSettings(BaseSettings):
    db_url: str = "sqlite+aiosqlite:///database.db"
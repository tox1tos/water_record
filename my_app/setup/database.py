from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.orm import sessionmaker, declarative_base
import os

Base = declarative_base()

class DatabaseManager:
    def __init__(self, database_url: str):
        self.engine = create_async_engine(database_url)
        self.SessionLocal = sessionmaker(
            bind=self.engine,
            class_=AsyncSession,
            expire_on_commit=False
        )

    async def initialize(self):
        async with self.engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

    async def dispose(self):
        await self.engine.dispose()

    async def get_db(self):
        async with self.SessionLocal() as session:
            yield session
import os
from contextlib import asynccontextmanager
from typing import AsyncGenerator

from dotenv import load_dotenv
from sqlalchemy.ext.asyncio import AsyncSession, async_sessionmaker, create_async_engine
from sqlalchemy.orm import DeclarativeBase

load_dotenv()


class Base(DeclarativeBase):
    pass


class DatabaseManager:
    def __init__(self, db_url: str):
        self._db_url = db_url
        self._engine = None
        self._session_maker = None

    async def initialize(self):
        if self._engine is not None:
            return
        self._engine = create_async_engine(self._db_url, echo=True)
        self._session_maker = async_sessionmaker(
            bind=self._engine, expire_on_commit=False, class_=AsyncSession
        )
        async with self._engine.begin() as conn:
            await conn.run_sync(Base.metadata.create_all)

    async def dispose(self):
        if self._engine:
            await self._engine.dispose()

    @asynccontextmanager
    async def get_session(self) -> AsyncGenerator[AsyncSession, None]:
        async with self._session_maker() as session:
            try:
                yield session
                await session.commit()
            except Exception:
                await session.rollback()
                raise


db_url = os.getenv("DATABASE_URL", "sqlite+aiosqlite:///./test.db")
database = DatabaseManager(db_url)


async def get_db() -> AsyncGenerator[AsyncSession, None]:
    await database.initialize()
    async with database.get_session() as session:
        yield session

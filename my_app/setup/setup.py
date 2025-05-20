from contextlib import asynccontextmanager
from typing import cast

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from my_app.core.repository import HydrationRepository
from my_app.core.router import (
    HydrationService,  # noqa: F811
    users_router,
)
from my_app.core.servicies import HydrationService  # noqa: F811
from my_app.operations.repository import HydrationRecordRepository
from my_app.operations.router import records_router
from my_app.operations.service import HydrationRecordService
from my_app.setup.database import DatabaseManager
from my_app.setup.settings import AppSettings


def setup_app() -> FastAPI:
    app = FastAPI(
        title="Hydration Tracker",
        description="API для отслеживания потребления воды",
        version="1.0.0",
        lifespan=app_lifetime,
    )

    app.add_middleware(
        CORSMiddleware,
        allow_origins=["*"],
        allow_methods=["*"],
        allow_headers=["*"],
        allow_credentials=True,
    )

    app.include_router(users_router, prefix="/api/user", tags=["user"])
    app.include_router(records_router, prefix="/api/hydration", tags=["hydration"])

    settings = AppSettings()

    app.state.db_manager = DatabaseManager(settings.db_url)

    app.state.user_service = HydrationService(HydrationRepository())
    app.state.hydration_service = HydrationRecordService(HydrationRecordRepository())

    return app


@asynccontextmanager
async def app_lifetime(app: FastAPI):
    db_manager = cast(DatabaseManager, app.state.db_manager)

    await db_manager.initialize()

    yield

    await db_manager.dispose()

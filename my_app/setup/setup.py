import logging
import logging.config
from contextlib import asynccontextmanager
from typing import cast

import yaml
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from ..core.repository import HydrationRepository
from ..core.router import users_router
from ..core.servicies import HydrationService
from ..operations.router import records_router
from ..operations.service import HydrationRecordService
from ..setup.database import DatabaseManager
from ..setup.settings import AppSettings

logger = logging.getLogger(__name__)


@asynccontextmanager
async def app_lifetime(app: FastAPI):
    """Функция должна быть определена ДО использования в FastAPI"""
    db_manager = cast(DatabaseManager, app.state.db_manager)
    logger.info("Starting app...")
    await db_manager.initialize()
    logger.info("Started")
    yield
    logger.info("Stopping app...")
    await db_manager.dispose()
    logger.info("Stopped")


def setup_app() -> FastAPI:
    try:
        with open("config.yaml") as f:
            d = yaml.load(f, yaml.FullLoader)
            logging.config.dictConfig(d)
    except FileNotFoundError:
        logging.basicConfig(level=logging.INFO)
        logger.warning(
            "config.yaml не найден, используется базовая настройка логирования"
        )

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

    app_settings = AppSettings()
    db = DatabaseManager(app_settings.db_url)

    app.state.db_manager = db
    app.state.user_service = HydrationService(HydrationRepository(db))
    app.state.hydration_service = HydrationRecordService(db)

    return app

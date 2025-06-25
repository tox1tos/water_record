from datetime import date

from fastapi import APIRouter, Depends
from sqlalchemy.ext.asyncio import AsyncSession

from ..core.controller import HydrationController
from ..core.repository import HydrationRepository
from ..core.schema import HydrationRecord, HydrationRecordCreate
from ..core.servicies import HydrationService
from ..setup.database import get_db

users_router = APIRouter()


@users_router.post("/hydration/", response_model=HydrationRecord)
async def add_record(record: HydrationRecordCreate, db: AsyncSession = Depends(get_db)):
    hydration_repository = HydrationRepository(db)
    hydration_service = HydrationService(hydration_repository)
    hydration_controller = HydrationController(hydration_service)
    return await hydration_controller.add_record(record)


@users_router.get("/hydration/", response_model=list[HydrationRecord])
async def get_records(
    start_date: date, end_date: date, db: AsyncSession = Depends(get_db)
):
    hydration_repository = HydrationRepository(db)
    hydration_service = HydrationService(hydration_repository)
    hydration_controller = HydrationController(hydration_service)
    return await hydration_controller.get_records(start_date, end_date)


@users_router.get("/hydration/total/")
async def get_total_water(
    start_date: date, end_date: date, db: AsyncSession = Depends(get_db)
):
    hydration_repository = HydrationRepository(db)
    hydration_service = HydrationService(hydration_repository)
    hydration_controller = HydrationController(hydration_service)
    total = await hydration_controller.get_total_water(start_date, end_date)
    return {"total_water": total}


@users_router.get("/hydration/report/")
async def get_report(
    start_date: date, end_date: date, db: AsyncSession = Depends(get_db)
):
    hydration_repository = HydrationRepository(db)
    hydration_service = HydrationService(hydration_repository)
    hydration_controller = HydrationController(hydration_service)
    report = await hydration_controller.get_hydration_report(start_date, end_date)
    return {"report": report}

from datetime import date

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..core.controller import HydrationController
from ..core.repository import HydrationRepository
from ..core.schema import HydrationRecord, HydrationRecordCreate
from ..core.servicies import HydrationService
from ..setup.database import DatabaseManager

users_router = APIRouter()


def get_db():
    db = DatabaseManager()
    try:
        yield db
    finally:
        db.close()


@users_router.post("/hydration/", response_model=HydrationRecord)
def add_record(record: HydrationRecordCreate, db: Session = Depends(get_db)):
    hydration_repository = HydrationRepository(db)
    hydration_service = HydrationService(hydration_repository)
    hydration_controller = HydrationController(hydration_service)
    return hydration_controller.add_record(record)


@users_router.get("/hydration/", response_model=list[HydrationRecord])
def get_records(start_date: date, end_date: date, db: Session = Depends(get_db)):
    hydration_repository = HydrationRepository(db)
    hydration_service = HydrationService(hydration_repository)
    hydration_controller = HydrationController(hydration_service)
    return hydration_controller.get_records(start_date, end_date)

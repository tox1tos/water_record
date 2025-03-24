from fastapi import APIRouter, Depends
from core.controller import HydrationController
from core.servicies import HydrationService
from core.repository import HydrationRepository
from sqlalchemy.orm import Session
from core.schema import HydrationRecordCreate, HydrationRecord
from datetime import date
from setup.database import SessionLocal

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/hydration/", response_model=HydrationRecord)
def add_record(record: HydrationRecordCreate, db: Session = Depends(get_db)):
    hydration_repository = HydrationRepository(db)
    hydration_service = HydrationService(hydration_repository)
    hydration_controller = HydrationController(hydration_service)
    return hydration_controller.add_record(record)

@router.get("/hydration/", response_model=list[HydrationRecord])
def get_records(start_date: date, end_date: date, db: Session = Depends(get_db)):
    hydration_repository = HydrationRepository(db)
    hydration_service = HydrationService(hydration_repository)
    hydration_controller = HydrationController(hydration_service)
    return hydration_controller.get_records(start_date, end_date)
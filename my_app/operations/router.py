from datetime import datetime
from fastapi import APIRouter, Depends
from pytest import Session
from my_app.operations.schema import HydrationRecordCreate, HydrationRecord
from my_app.setup.database import get_db

router = APIRouter()

@router.post("/", response_model=HydrationRecord)
async def add_record(
    record: HydrationRecordCreate, 
    db: Session = Depends(get_db)
):
    pass

@router.get("/", response_model=list[HydrationRecord])
async def get_records(
    user_id: int,
    start: datetime,
    end: datetime,
    db: Session = Depends(get_db)
):
    pass
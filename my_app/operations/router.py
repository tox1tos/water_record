from datetime import datetime

from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

from ..operations.schema import HydrationRecord, HydrationRecordCreate
from ..setup.database import get_db

records_router = APIRouter()


@records_router.post("/", response_model=HydrationRecord)
async def add_record(record: HydrationRecordCreate, db: Session = Depends(get_db)):
    pass


@records_router.get("/", response_model=list[HydrationRecord])
async def get_records(
    user_id: int, start: datetime, end: datetime, db: Session = Depends(get_db)
):
    pass

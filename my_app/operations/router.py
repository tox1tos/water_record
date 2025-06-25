from datetime import datetime

from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.ext.asyncio import AsyncSession

from ..operations.schema import HydrationRecord, HydrationRecordCreate
from ..operations.service import HydrationRecordService
from ..setup.database import get_db

records_router = APIRouter()


@records_router.post("/", response_model=HydrationRecord)
async def add_record(record: HydrationRecordCreate, db: AsyncSession = Depends(get_db)):
    service = HydrationRecordService(db)
    try:
        return await service.create_record(record.user_id, record.amount)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


@records_router.get("/", response_model=list[HydrationRecord])
async def get_records(
    user_id: int, start: datetime, end: datetime, db: AsyncSession = Depends(get_db)
):
    service = HydrationRecordService(db)
    try:
        return await service.get_records(user_id, start, end)
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

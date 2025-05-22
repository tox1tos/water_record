from datetime import datetime

from pydantic import BaseModel


class HydrationRecordBase(BaseModel):
    amount: int
    timestamp: datetime


class HydrationRecordCreate(HydrationRecordBase):
    pass


class HydrationRecord(HydrationRecordBase):
    id: int
    user_id: int

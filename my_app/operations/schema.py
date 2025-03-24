# hydration/records/schemas.py
from pydantic import BaseModel
from datetime import datetime

class HydrationRecordBase(BaseModel):
    amount: int
    timestamp: datetime

class HydrationRecordCreate(HydrationRecordBase):
    pass

class HydrationRecord(HydrationRecordBase):
    id: int
    user_id: int
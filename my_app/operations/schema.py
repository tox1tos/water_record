from datetime import datetime
from typing import Optional

from pydantic import BaseModel, Field


class HydrationRecordBase(BaseModel):
    amount: int
    user_id: int
    timestamp: Optional[datetime] = Field(default=None)


class HydrationRecordCreate(HydrationRecordBase):
    user_id: int


class HydrationRecord(HydrationRecordBase):
    id: int
    user_id: int

    class Config:
        orm_mode = True

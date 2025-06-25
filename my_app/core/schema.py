import datetime

from pydantic import BaseModel


class HydrationRecordBase(BaseModel):
    date: datetime.date
    glasses: int
    amount: int


class HydrationRecordCreate(HydrationRecordBase):
    user_id: int


class HydrationRecord(HydrationRecordBase):
    id: int

    class Config:
        from_attributes = True

from datetime import date

from pydantic import BaseModel


class HydrationRecordBase(BaseModel):
    date: date
    glasses: int


class HydrationRecordCreate(HydrationRecordBase):
    pass


class HydrationRecord(HydrationRecordBase):
    id: int

    class Config:
        from_attributes = True

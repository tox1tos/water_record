from pydantic import BaseModel
from datetime import date

class HydrationRecordBase(BaseModel):
    date: date
    glasses: int

class HydrationRecordCreate(HydrationRecordBase):
    pass

class HydrationRecord(HydrationRecordBase):
    id: int

    class Config:
        orm_mode = True

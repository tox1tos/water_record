from sqlalchemy.orm import Session
from core.models import HydrationRecord
from core.schema import HydrationRecordCreate
from datetime import date

class HydrationRepository:
    def __init__(self, db: Session):
        self.db = db

    def create_record(self, record: HydrationRecordCreate):
        db_record = HydrationRecord(date=record.date, glasses=record.glasses)
        self.db.add(db_record)
        self.db.commit()
        self.db.refresh(db_record)
        return db_record

    def get_records(self, start_date: date, end_date: date):
        return self.db.query(HydrationRecord).filter(HydrationRecord.date >= start_date, HydrationRecord.date <= end_date).all()
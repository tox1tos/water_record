from sqlalchemy.orm import Session
from sqlalchemy import select, func, between
from datetime import datetime
from typing import List
from my_app.operations.models import HydrationRecord

class HydrationRecordRepository:
    def __init__(self, db: Session):
        self.db = db

    async def create_record(self, user_id: int, amount: int) -> HydrationRecord:
        new_record = HydrationRecord(
            user_id=user_id,
            amount=amount,
            timestamp=datetime.utcnow()
        )
        self.db.add(new_record)
        await self.db.commit()
        await self.db.refresh(new_record)
        return new_record

    async def get_records(
        self, 
        user_id: int,
        start_date: datetime,
        end_date: datetime
    ) -> List[HydrationRecord]:
        result = await self.db.execute(
            select(HydrationRecord)
            .where(
                (HydrationRecord.user_id == user_id) &
                between(HydrationRecord.timestamp, start_date, end_date)
            )
            .order_by(HydrationRecord.timestamp)
        )
        return result.scalars().all()

    async def get_daily_summary(
        self,
        user_id: int,
        date: datetime
    ) -> int:
        result = await self.db.execute(
            select(func.sum(HydrationRecord.amount))
            .where(
                (HydrationRecord.user_id == user_id) &
                (func.date(HydrationRecord.timestamp) == date.date())
            )
        )
        return result.scalar() or 0
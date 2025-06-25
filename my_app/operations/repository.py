from datetime import datetime
from typing import List

from sqlalchemy import between, func, select

from ..operations.models import HydrationRecord


class HydrationRecordRepository:
    def __init__(self, db_manager):
        self.db_manager = db_manager

    async def create_record(self, user_id: int, amount: int) -> HydrationRecord:
        session = self.db_manager  # <- просто используй её как есть

        now = datetime.utcnow()
        glasses = amount // 250
        new_record = HydrationRecord(
            user_id=user_id,
            amount=amount,
            glasses=glasses,
            timestamp=now,
            date=now.date(),
        )
        session.add(new_record)
        await session.commit()
        await session.refresh(new_record)
        return new_record

    async def get_records(
        self, user_id: int, start_date: datetime, end_date: datetime
    ) -> List[HydrationRecord]:
        result = await self.db_manager.execute(
            select(HydrationRecord)
            .where(
                (HydrationRecord.user_id == user_id)
                & between(HydrationRecord.timestamp, start_date, end_date)
            )
            .order_by(HydrationRecord.timestamp)
        )
        return result.scalars().all()

    async def get_daily_summary(self, user_id: int, date: datetime) -> int:
        result = await self.db_manager.execute(
            select(func.sum(HydrationRecord.amount)).where(
                (HydrationRecord.user_id == user_id)
                & (func.date(HydrationRecord.timestamp) == date.date())
            )
        )
        return result.scalar() or 0

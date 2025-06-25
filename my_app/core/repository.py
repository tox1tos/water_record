from datetime import date

from sqlalchemy import select
from sqlalchemy.ext.asyncio import AsyncSession

from ..core.schema import HydrationRecordCreate
from ..operations.models import HydrationRecord


class HydrationRepository:
    def __init__(self, session: AsyncSession):
        self.session = session

    async def create_record(self, record: HydrationRecordCreate):
        print(">>> create_record called in HydrationRepository")
        db_record = HydrationRecord(
            date=record.date,
            glasses=record.glasses,
            amount=record.amount,
            user_id=record.user_id,
        )
        self.session.add(db_record)
        await self.session.commit()
        await self.session.refresh(db_record)

        return db_record

    async def get_records(self, start_date: date, end_date: date):
        print(">>> get_records called in HydrationRepository")
        stmt = select(HydrationRecord).where(
            HydrationRecord.date >= start_date, HydrationRecord.date <= end_date
        )
        result = await self.session.execute(stmt)
        records = result.scalars().all()
        return records

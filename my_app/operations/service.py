from datetime import datetime
from typing import List

from sqlalchemy.ext.asyncio import AsyncSession

from ..operations.models import HydrationRecord
from ..operations.repository import HydrationRecordRepository


class HydrationRecordService:
    def __init__(self, session: AsyncSession):
        self.repository = HydrationRecordRepository(session)

    async def create_record(self, user_id: int, amount: int) -> HydrationRecord:
        return await self.repository.create_record(user_id, amount)

    async def get_records(
        self, user_id: int, start_date: datetime, end_date: datetime
    ) -> List[HydrationRecord]:
        return await self.repository.get_records(user_id, start_date, end_date)

    async def get_daily_summary(self, user_id: int, date: datetime) -> int:
        return await self.repository.get_daily_summary(user_id, date)

from datetime import date
from typing import List

from ..core.repository import HydrationRepository
from ..core.schema import HydrationRecord, HydrationRecordCreate
from ..operations.hydration_operations import (
    calculate_total_water,
    generate_hydration_report,
)


class HydrationService:
    def __init__(self, hydration_repository: HydrationRepository):
        self.hydration_repository = hydration_repository

    async def add_record(self, record: HydrationRecordCreate) -> HydrationRecord:
        return await self.hydration_repository.create_record(record)

    async def get_records(
        self, start_date: date, end_date: date
    ) -> List[HydrationRecord]:
        return await self.hydration_repository.get_records(start_date, end_date)

    async def get_total_water(self, start_date: date, end_date: date) -> int:
        records = await self.get_records(start_date, end_date)
        return calculate_total_water(records)

    async def get_hydration_report(self, start_date: date, end_date: date) -> str:
        records = await self.get_records(start_date, end_date)
        return generate_hydration_report(records)

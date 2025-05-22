from datetime import date
from typing import List

from fastapi import HTTPException

from ..core.schema import HydrationRecord, HydrationRecordCreate
from ..core.servicies import HydrationService


class HydrationController:
    def __init__(self, hydration_service: HydrationService):
        self.hydration_service = hydration_service

    def add_record(self, record: HydrationRecordCreate) -> HydrationRecord:
        return self.hydration_service.add_record(record)

    def get_records(self, start_date: date, end_date: date) -> List[HydrationRecord]:
        records = self.hydration_service.get_records(start_date, end_date)
        if not records:
            raise HTTPException(status_code=404, detail="No records found")
        return records

    def get_total_water(self, start_date: date, end_date: date) -> int:
        return self.hydration_service.get_total_water(start_date, end_date)

    def get_hydration_report(self, start_date: date, end_date: date) -> str:
        return self.hydration_service.get_hydration_report(start_date, end_date)

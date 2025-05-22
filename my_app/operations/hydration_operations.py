from collections import defaultdict
from datetime import date
from typing import Dict, List

from ..core.schema import HydrationRecord


def calculate_total_water(records: List[HydrationRecord]) -> int:
    """
    Возвращает общее количество выпитой воды за период.
    """
    return sum(record.glasses for record in records)


def calculate_average_water_per_day(records: List[HydrationRecord]) -> float:
    """
    Возвращает среднее количество стаканов воды за день.
    """
    if not records:
        return 0.0
    sorted_records = sorted(records, key=lambda r: r.date)
    total_glasses = calculate_total_water(sorted_records)
    days = (sorted_records[-1].date - sorted_records[0].date).days + 1
    return total_glasses / days


def generate_hydration_report(records: List[HydrationRecord]) -> str:
    """
    Генерирует текстовый отчет о гидрации.
    """
    if not records:
        return "No records found."

    total_glasses = calculate_total_water(records)
    average_glasses = calculate_average_water_per_day(records)
    start_date = records[0].date
    end_date = records[-1].date

    report = (
        f"Hydration Report from {start_date} to {end_date}:\n"
        f"Total glasses: {total_glasses}\n"
        f"Average glasses per day: {average_glasses:.2f}\n"
    )
    return report


def get_daily_water_stats(records: List[HydrationRecord]) -> Dict[date, int]:
    """
    Возвращает количество стаканов воды за каждый день в промежутке.
    """
    daily_stats = defaultdict(int)
    for record in records:
        daily_stats[record.date] += record.glasses
    return dict(daily_stats)

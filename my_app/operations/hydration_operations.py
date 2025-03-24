from datetime import date
from typing import List
from core.schema import HydrationRecord

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
    total_glasses = calculate_total_water(records)
    days = (records[-1].date - records[0].date).days + 1
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
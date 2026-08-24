#--------------------Data Structures And Business Applications------------------------
#------------------------------Semester Project---------------------------------------
#BSBA-5B
#Rayyan Asim(23i-5002),Sohaib Safdar(23i-5030)
#Topic 25: Fleet Fuel Optimization

# models.py
from typing import List

class FuelLog:
    def __init__(self, date: str, fuel: float, distance: float, note: str = ""):
        self.date = date
        self.fuel = float(fuel)
        self.distance = float(distance)
        self.note = note

class Vehicle:
    def __init__(self, vehicle_id: str, total_distance: float = 0.0,
                 total_fuel: float = 0.0, last_service_date: str = ""):
        self.vehicle_id = vehicle_id
        self.total_distance = float(total_distance)
        self.total_fuel = float(total_fuel)
        self.last_service_date = last_service_date
        self.logs: List[FuelLog] = []
        self.efficiency: float = 0.0

    def add_log(self, fuel: float, distance: float, date: str, note: str = "") -> None:
        log = FuelLog(date=date, fuel=fuel, distance=distance, note=note)
        self.logs.append(log)
        self.total_fuel += float(fuel)
        self.total_distance += float(distance)

    def compute_efficiency(self) -> None:
        if self.total_fuel <= 0:
            self.efficiency = 0.0
        else:
            self.efficiency = self.total_distance / self.total_fuel

    def to_simple_dict(self) -> dict:
        return {
            "vehicle_id": self.vehicle_id,
            "total_distance": self.total_distance,
            "total_fuel": self.total_fuel,
            "efficiency": self.efficiency,
            "last_service_date": self.last_service_date,
        }

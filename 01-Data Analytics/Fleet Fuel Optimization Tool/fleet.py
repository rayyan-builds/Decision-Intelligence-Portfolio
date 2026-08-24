#--------------------Data Structures And Business Applications------------------------
#------------------------------Semester Project---------------------------------------
#BSBA-5B
#Rayyan Asim(23i-5002),Sohaib Safdar(23i-5030)
#Topic 25: Fleet Fuel Optimization

# fleet.py
from typing import List, Optional, Tuple, Callable
from models import Vehicle
from sorting import sort_by_key
from heap_impl import build_max_heap, heap_pop
import csv

class FleetManager:
    def __init__(self):
        self.vehicles: List[Vehicle] = []

    # ---- CRUD ----
    def add_vehicle(self, vehicle: Vehicle) -> None:
        # check duplicate
        for v in self.vehicles:
            if v.vehicle_id == vehicle.vehicle_id:
                raise ValueError("Vehicle ID exists")
        self.vehicles.append(vehicle)

    def remove_vehicle(self, vehicle_id: str) -> bool:
        idx = None
        for i in range(len(self.vehicles)):
            if self.vehicles[i].vehicle_id == vehicle_id:
                idx = i
                break
        if idx is None:
            return False
        # swap with last then pop
        last = len(self.vehicles) - 1
        if idx != last:
            self.vehicles[idx] = self.vehicles[last]
        self.vehicles.pop()
        return True

    def add_fuel_log(self, vehicle_id: str, fuel: float, distance: float, date: str, note: str = "") -> bool:
        for v in self.vehicles:
            if v.vehicle_id == vehicle_id:
                v.add_log(fuel=fuel, distance=distance, date=date, note=note)
                return True
        return False

    # ---- metrics ----
    def recompute_all_metrics(self) -> None:
        for v in self.vehicles:
            v.compute_efficiency()

    # ---- searching ----
    def linear_search_by_id(self, vehicle_id: str) -> Tuple[Optional[Vehicle], int]:
        visits = 0
        for v in self.vehicles:
            visits += 1
            if v.vehicle_id == vehicle_id:
                return v, visits
        return None, visits

    def binary_search_by_key(self, arr: List[Vehicle], key_func: Callable[[Vehicle], float], value: float) -> Tuple[Optional[Vehicle], int]:
        # arr must be sorted ascending by key_func
        left = 0
        right = len(arr) - 1
        visits = 0
        while left <= right:
            mid = (left + right) // 2
            visits += 1
            mid_val = key_func(arr[mid])
            if mid_val == value:
                return arr[mid], visits
            if mid_val < value:
                left = mid + 1
            else:
                right = mid - 1
        return None, visits

    # ---- sorting views ----
    def get_sorted_by_efficiency(self, descending: bool = True) -> List[Vehicle]:
        self.recompute_all_metrics()
        # returns new list, original self.vehicles unchanged
        return sort_by_key(self.vehicles, key=lambda x: x.efficiency, descending=descending)

    def get_sorted_by_total_fuel(self, descending: bool = True) -> List[Vehicle]:
        return sort_by_key(self.vehicles, key=lambda x: x.total_fuel, descending=descending)

    # ---- top-k using heap (non-destructive) ----
    def top_k_worst_by_efficiency(self, k: int) -> List[Vehicle]:
        self.recompute_all_metrics()
        # priority = -efficiency => lower efficiency -> higher priority number (more negative)
        items = []
        for v in self.vehicles:
            items.append( (-v.efficiency, v) )
        heap = build_max_heap(items, key=lambda x: x[0])
        res = []
        count = k if k <= len(heap) else len(heap)
        for _ in range(count):
            prio, v = heap_pop(heap, key=lambda x: x[0])
            res.append(v)
        return res

    def top_k_by_total_fuel(self, k: int) -> List[Vehicle]:
        items = []
        for v in self.vehicles:
            items.append( (v.total_fuel, v) )
        heap = build_max_heap(items, key=lambda x: x[0])
        res = []
        count = k if k <= len(heap) else len(heap)
        for _ in range(count):
            prio, v = heap_pop(heap, key=lambda x: x[0])
            res.append(v)
        return res

    # ---- CSV I/O (simple) ----
    def load_from_csv(self, filename: str) -> None:
        with open(filename, newline='') as f:
            reader = csv.DictReader(f)
            for row in reader:
                vid = row.get("vehicle_id", "").strip()
                if vid == "":
                    continue
                td = float(row.get("total_distance", 0) or 0)
                tf = float(row.get("total_fuel", 0) or 0)
                lsd = row.get("last_service_date", "")
                v = Vehicle(vehicle_id=vid, total_distance=td, total_fuel=tf, last_service_date=lsd)
                self.add_vehicle(v)
        self.recompute_all_metrics()

    def save_to_csv(self, filename: str) -> None:
        with open(filename, "w", newline='') as f:
            fieldnames = ["vehicle_id", "total_distance", "total_fuel", "efficiency", "last_service_date"]
            writer = csv.DictWriter(f, fieldnames=fieldnames)
            writer.writeheader()
            for v in self.vehicles:
                writer.writerow({
                    "vehicle_id": v.vehicle_id,
                    "total_distance": v.total_distance,
                    "total_fuel": v.total_fuel,
                    "efficiency": v.efficiency,
                    "last_service_date": v.last_service_date
                })

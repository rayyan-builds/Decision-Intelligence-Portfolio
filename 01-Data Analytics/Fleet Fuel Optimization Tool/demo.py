#--------------------Data Structures And Business Applications------------------------
#------------------------------Semester Project---------------------------------------
#BSBA-5B
#Rayyan Asim(23i-5002),Sohaib Safdar(23i-5030)
#Topic 25: Fleet Fuel Optimization

# demo.py
from fleet import FleetManager
from models import Vehicle
from datetime import date

def pretty_print_list(title: str, vehicles):
    print("----", title, "----")
    for v in vehicles:
        print(f"ID: {v.vehicle_id} | dist: {v.total_distance:.1f} | fuel: {v.total_fuel:.1f} | eff: {v.efficiency:.3f}")

def demo():
    m = FleetManager()
    # add sample vehicles
    m.add_vehicle(Vehicle("V001", total_distance=1200, total_fuel=100, last_service_date="2025-06-01"))
    m.add_vehicle(Vehicle("V002", total_distance=900, total_fuel=120, last_service_date="2025-05-20"))
    m.add_vehicle(Vehicle("V003", total_distance=500, total_fuel=80, last_service_date="2025-04-10"))
    m.add_vehicle(Vehicle("V004", total_distance=300, total_fuel=50, last_service_date="2025-07-01"))
    m.add_vehicle(Vehicle("V005", total_distance=1600, total_fuel=200, last_service_date="2025-03-01"))
    m.recompute_all_metrics()

    best = m.get_sorted_by_efficiency(descending=True)
    pretty_print_list("Sorted by efficiency (best first)", best)

    worst3 = m.top_k_worst_by_efficiency(3)
    pretty_print_list("Top 3 worst by efficiency", worst3)

    found, visits = m.linear_search_by_id("V003")
    if found:
        print(f"\nFound V003 in {visits} visits, efficiency: {found.efficiency:.3f}")
    else:
        print("V003 not found")

    # Add a log
    m.add_fuel_log("V003", fuel=20, distance=120, date=str(date.today()))
    m.recompute_all_metrics()
    v, _ = m.linear_search_by_id("V003")
    print(f"\nAfter adding log for V003 -> dist: {v.total_distance}, fuel: {v.total_fuel}, eff: {v.efficiency:.3f}")

if __name__ == "__main__":
    demo()

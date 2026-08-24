#--------------------Data Structures And Business Applications------------------------
#------------------------------Semester Project---------------------------------------
#BSBA-5B
#Rayyan Asim(23i-5002),Sohaib Safdar(23i-5030)
#Topic 25: Fleet Fuel Optimization

# interactive_demo.py
# Interactive CLI for Fleet Fuel Optimization Tool
# Allows unlimited user entries until user picks Exit.

from fleet import FleetManager
from models import Vehicle
from datetime import date


def read_non_empty(prompt: str) -> str:
    while True:
        s = input(prompt).strip()
        if s != "":
            return s
        print("Input cannot be empty. Try again.")

def read_float(prompt: str) -> float:
    while True:
        s = input(prompt).strip()
        try:
            val = float(s)
            return val
        except ValueError:
            print("Enter a valid number (e.g., 123.45).")

def read_int(prompt: str, min_val: int = None, max_val: int = None) -> int:
    while True:
        s = input(prompt).strip()
        try:
            v = int(s)
            if min_val is not None and v < min_val:
                print(f"Enter a number >= {min_val}.")
                continue
            if max_val is not None and v > max_val:
                print(f"Enter a number <= {max_val}.")
                continue
            return v
        except ValueError:
            print("Enter a valid integer.")

def print_vehicle_summary(v):
    print(f"ID: {v.vehicle_id} | dist: {v.total_distance:.1f} | fuel: {v.total_fuel:.1f} | eff: {v.efficiency:.3f} | last_service: {v.last_service_date}")

def print_list(title: str, lst):
    print("=== " + title + " ===")
    if not lst:
        print("(empty)")
    for item in lst:
        print_vehicle_summary(item)

def menu_text():
    print("\nFleet Manager - Interactive CLI")
    print("1) Add new vehicle")
    print("2) Remove vehicle")
    print("3) Add fuel log to vehicle")
    print("4) Show all vehicles (unsorted)")
    print("5) Show sorted by efficiency")
    print("6) Show sorted by total fuel")
    print("7) Show top-k worst by efficiency")
    print("8) Search vehicle by ID (linear)")
    print("9) Load from CSV file")
    print("10) Save to CSV file")
    print("11) Recompute metrics (manual)")
    print("12) Exit")
    print()

def handle_add_vehicle(manager: FleetManager):
    vid = read_non_empty("Enter vehicle ID (unique): ")
    td = read_float("Enter total distance (or 0): ")
    tf = read_float("Enter total fuel (or 0): ")
    lsd = input("Enter last service date (YYYY-MM-DD) or leave blank: ").strip()
    try:
        v = Vehicle(vehicle_id=vid, total_distance=td, total_fuel=tf, last_service_date=lsd)
        manager.add_vehicle(v)
        manager.recompute_all_metrics()
        print("Vehicle added.")
    except ValueError as e:
        print("Error:", e)

def handle_remove_vehicle(manager: FleetManager):
    vid = read_non_empty("Enter vehicle ID to remove: ")
    ok = manager.remove_vehicle(vid)
    if ok:
        print("Removed.")
    else:
        print("Vehicle not found.")

def handle_add_log(manager: FleetManager):
    vid = read_non_empty("Enter vehicle ID to add log: ")
    fuel = read_float("Enter fuel used (liters): ")
    dist = read_float("Enter distance (km): ")
    dat = input("Enter date (YYYY-MM-DD) or leave blank for today: ").strip()
    if dat == "":
        dat = str(date.today())
    note = input("Optional note: ").strip()
    ok = manager.add_fuel_log(vid, fuel=fuel, distance=dist, date=dat, note=note)
    if ok:
        manager.recompute_all_metrics()
        print("Log added and metrics updated.")
    else:
        print("Vehicle not found. Use Add new vehicle first.")

def handle_show_all(manager: FleetManager):
    if not manager.vehicles:
        print("(no vehicles)")
        return
    print("All vehicles (in insertion order):")
    for v in manager.vehicles:
        print_vehicle_summary(v)

def handle_show_sorted_eff(manager: FleetManager):
    order = input("Order - (a)scending or (d)escending? [d]: ").strip().lower()
    descending = True
    if order == "a":
        descending = False
    manager.recompute_all_metrics()
    lst = manager.get_sorted_by_efficiency(descending=descending)
    print_list("Sorted by efficiency", lst)

def handle_show_sorted_fuel(manager: FleetManager):
    order = input("Order - (a)scending or (d)escending? [d]: ").strip().lower()
    descending = True
    if order == "a":
        descending = False
    lst = manager.get_sorted_by_total_fuel(descending=descending)
    print_list("Sorted by total fuel", lst)

def handle_top_k_worst(manager: FleetManager):
    if not manager.vehicles:
        print("(no vehicles)")
        return
    k = read_int("Enter k (top k worst): ", min_val=1)
    lst = manager.top_k_worst_by_efficiency(k)
    print_list(f"Top {k} worst by efficiency (lowest efficiency first)", lst)

def handle_search(manager: FleetManager):
    vid = read_non_empty("Enter vehicle ID to search: ")
    v, visits = manager.linear_search_by_id(vid)
    if v is None:
        print(f"Vehicle not found. Visits: {visits}")
    else:
        print(f"Found in {visits} visits:")
        print_vehicle_summary(v)

def handle_load_csv(manager: FleetManager):
    fname = read_non_empty("Enter CSV filename to load: ")
    try:
        manager.load_from_csv(fname)
        manager.recompute_all_metrics()
        print("Loaded.")
    except FileNotFoundError:
        print("File not found.")
    except Exception as e:
        print("Error while loading:", e)

def handle_save_csv(manager: FleetManager):
    fname = read_non_empty("Enter CSV filename to save: ")
    try:
        manager.save_to_csv(fname)
        print("Saved.")
    except Exception as e:
        print("Error while saving:", e)

def main_loop():
    manager = FleetManager()
    print("Interactive Fleet Manager")
    print("You can keep adding entries without limit. Exit when you want.\n")
    while True:
        try:
            menu_text()
            choice = input("Choose an option (1-12): ").strip()
            if choice == "1":
                handle_add_vehicle(manager)
            elif choice == "2":
                handle_remove_vehicle(manager)
            elif choice == "3":
                handle_add_log(manager)
            elif choice == "4":
                handle_show_all(manager)
            elif choice == "5":
                handle_show_sorted_eff(manager)
            elif choice == "6":
                handle_show_sorted_fuel(manager)
            elif choice == "7":
                handle_top_k_worst(manager)
            elif choice == "8":
                handle_search(manager)
            elif choice == "9":
                handle_load_csv(manager)
            elif choice == "10":
                handle_save_csv(manager)
            elif choice == "11":
                manager.recompute_all_metrics()
                print("Metrics recomputed.")
            elif choice == "12":
                print("Exiting. Goodbye.")
                break
            else:
                print("Invalid choice. Pick 1-12.")
        except KeyboardInterrupt:
            print("\nKeyboard interrupt detected. Exiting.")
            break
        except Exception as ee:
            print("An error occurred:", ee)

if __name__ == "__main__":
    main_loop()

# 🚛 Fleet Fuel Optimization Tool

### Data Structures and Business Applications — Semester Project (Option 25)

A fleet management system that applies core data structures — **arrays, custom sorting algorithms, a binary heap, and search algorithms** — to solve a real logistics problem: efficiently monitoring, comparing, and prioritizing vehicles by fuel efficiency across a business fleet.

---

## 🎯 Problem Statement

Logistics, transportation, and delivery companies often rely on manual logs or spreadsheets to track vehicle fuel consumption. This makes it slow to locate specific vehicle records, identify fuel-inefficient vehicles, or catch irregular performance patterns — leading to higher operational costs, poor route assignments, and delayed maintenance decisions.

The **Fleet Fuel Optimization Tool** simulates a real-world fleet monitoring system used by logistics firms, courier services, and inter-city transport companies, organizing fuel data so that inefficiencies can be found and acted on quickly.

---

## 💼 Business Impact

- 🔍 **Instant lookups** — retrieve any vehicle's record without scanning the entire fleet.
- 📊 **Ranked comparisons** — sort the fleet by efficiency or fuel consumption to support route planning and driver performance evaluation.
- ⚠️ **Priority maintenance** — a heap-based structure surfaces the most fuel-inefficient vehicles instantly, so they can be prioritized for inspection.
- 💰 **Cost savings** — organized, data-driven insights reduce unnecessary fuel usage and improve resource allocation.

---

## 🛠️ Technology Stack

| Area | Tools |
|---|---|
| 🐍 Language | **Python** |
| 🗂️ Core Data Structure | Arrays (Python lists) of `Vehicle` objects |
| 🔃 Sorting | Custom **Merge Sort** + **Insertion Sort** hybrid (implemented from scratch) |
| ⛰️ Priority Queue | Custom **Binary Max-Heap** (implemented from scratch) |
| 🔎 Searching | **Linear Search** and **Binary Search** |
| 💾 Data I/O | CSV import/export |
| 🖥️ Interface | Interactive Command-Line Interface (CLI) |

<div align="center">

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Data Structures](https://img.shields.io/badge/Data%20Structures-2C5364?style=for-the-badge)
![Algorithms](https://img.shields.io/badge/Algorithms-2C5364?style=for-the-badge)
![CSV](https://img.shields.io/badge/CSV%20I%2FO-203A43?style=for-the-badge)

</div>

---

## 🧩 Data Structures Used

| Structure | Role in the Project |
|---|---|
| 📋 **Arrays** | Store structured `Vehicle` records — ID, distance, fuel, efficiency, service date |
| 🔃 **Merge Sort / Insertion Sort** | Generate ranked lists of vehicles by efficiency or fuel consumption (insertion sort used for small sub-lists ≤16 items) |
| ⛰️ **Binary Max-Heap** | Retrieve the top-*k* worst (or best) performing vehicles without a full sort |
| 🔎 **Linear & Binary Search** | Locate a specific vehicle by ID or by a sorted key value |

Each structure was implemented **from scratch** (no built-in `sort()`, `heapq`, or `bisect`) to demonstrate the underlying algorithmic mechanics rather than relying on Python's standard library.

---

## 📁 Project Structure

```text
Fleet Fuel Optimization Tool/
│
├── models.py              # Vehicle & FuelLog classes, efficiency calculation
├── sorting.py              # Custom insertion sort & merge sort implementations
├── heap_impl.py            # Custom binary max-heap (build, push, pop)
├── fleet.py                 # FleetManager — CRUD, search, sort, heap, CSV I/O
├── demo.py                  # Scripted demo showcasing core functionality
├── interactive_demo.py      # Interactive CLI for unlimited manual data entry
├── Project_Proposal.pdf     # Original project proposal
└── README.md
```

---

## ⚙️ Core Components

### `models.py`
Defines the `Vehicle` class (ID, total distance, total fuel, service date, fuel logs, computed efficiency) and `FuelLog` for individual refueling entries. Efficiency is computed as `total_distance / total_fuel`.

### `sorting.py`
- `insertion_sort()` — used directly for small lists (≤16 elements)
- `merge_sort()` — recursive merge sort, falling back to insertion sort below the threshold for practical efficiency
- `sort_by_key()` — public interface supporting ascending/descending order via a manual reversal pass

### `heap_impl.py`
A from-scratch binary max-heap with `heapify_up`, `heapify_down`, `build_max_heap`, `heap_push`, and `heap_pop` — used to extract the top-*k* worst (or best) vehicles by efficiency or fuel usage without sorting the entire fleet.

### `fleet.py`
The `FleetManager` class ties everything together:
- **CRUD:** `add_vehicle()`, `remove_vehicle()`, `add_fuel_log()`
- **Search:** `linear_search_by_id()`, `binary_search_by_key()`
- **Sorted views:** `get_sorted_by_efficiency()`, `get_sorted_by_total_fuel()`
- **Heap-based ranking:** `top_k_worst_by_efficiency()`, `top_k_by_total_fuel()`
- **Persistence:** `load_from_csv()`, `save_to_csv()`

---

## ▶️ Running the Project

### Scripted Demo
Runs a fixed set of sample vehicles through sorting, top-k heap ranking, and search operations:

```bash
python demo.py
```

### Interactive CLI
Lets you add, remove, search, sort, and rank an unlimited number of vehicles through a menu-driven interface:

```bash
python interactive_demo.py
```

**Menu options include:**
- Add / remove a vehicle
- Add a fuel log to an existing vehicle
- View all vehicles (unsorted)
- View vehicles sorted by efficiency or total fuel (ascending/descending)
- View the top-*k* worst-performing vehicles by efficiency
- Search for a vehicle by ID (linear search)
- Load / save fleet data from/to a CSV file
- Manually recompute efficiency metrics

---

## 🧪 Edge Case Handling

- 🚫 Duplicate vehicle IDs are rejected on insert
- ⚠️ Zero or missing fuel values are handled safely in efficiency calculations (avoids division by zero)
- ✅ Input validation for numeric fields in the interactive CLI (retries on invalid input)
- 📁 Missing CSV files are caught and reported without crashing the program

---

## 📊 Expected Output & Features

- Ranked vehicle lists by fuel efficiency or total fuel consumption
- Instant top-*k* identification of the most (or least) fuel-efficient vehicles
- Fast lookup of any vehicle's full record by ID
- CSV-based persistence for loading and saving fleet data between sessions

---

## 👥 Team

| Name | Roll Number |
|---|---|
| Rayyan Asim | 23i-5002 |
| Sohaib Safdar | 23i-5030 |

**Section:** BSBA-5B · **Course:** Data Structures and Business Applications · **Project Option:** 25 — Fleet Fuel Optimization Tool

# 📦 Inventory Simulation for a Pop-Up Store

### Fundamentals of Business Analytics — Discrete-Event Simulation with AnyLogic & Python

A simulation-based analytics project that models inventory operations for a short-term, 7-day pop-up retail store — determining the optimal initial stock, reorder point, and restock quantity to minimize total cost while maintaining a high service level, under tight constraints like limited storage capacity and a single restocking opportunity.

---

## 🎯 Problem Statement

A pop-up store operating for a 7-day window needs an inventory policy that minimizes stockouts and overstocking risk. Customer demand changes daily, and the store gets **only one restock opportunity** with a fixed 2-day lead time. Both holding excess inventory and losing sales carry real costs — the goal is to find the policy that keeps service levels high at the lowest total cost.

### Constraints

- 📐 Inventory capacity limited to **400 units**
- 🔁 Restock can only be placed **once** during the 7-day period
- ⏱️ Restock has a fixed **2-day delivery lead time**
- 📊 Demand for this simulation is deterministic and known ahead of time

---

## 📏 Key Performance Indicators (KPIs)

| KPI | Description |
|---|---|
| 🎯 Service Level (%) | Percentage of customer demand successfully fulfilled |
| 💰 Total Holding Cost ($) | Sum of daily holding costs ($1.50 per unit held per day) |
| 📉 Lost Sales Cost ($) | Sum of lost revenue due to stockouts ($20 per unfulfilled order) |
| 💵 Total Cost ($) | Combined holding and lost sales costs |

---

## 🛠️ Technology Stack

| Area | Tools |
|---|---|
| 🖥️ Simulation Engine | **AnyLogic Personal Learning Edition (PLE)** |
| 🧩 Modeling Approach | Discrete-Event Simulation (Process Modeling Library) |
| 🐍 Supplementary Analysis | **Python, Jupyter Notebook** |
| 📄 Data & Documentation | Excel, Word |

<div align="center">

![AnyLogic](https://img.shields.io/badge/AnyLogic-PLE-2C5364?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![Jupyter](https://img.shields.io/badge/Jupyter-F37626?style=for-the-badge&logo=jupyter&logoColor=white)
![Excel](https://img.shields.io/badge/Excel-217346?style=for-the-badge&logo=microsoftexcel&logoColor=white)

</div>

---

## 🧠 Modeling Approach

A discrete-event model was built using AnyLogic's **Process Modeling Library**, where customer demand is generated daily and compared against available inventory. Restocking is triggered once inventory falls below the reorder point.

### Key Entities & Parameters

- **Entities:** `RestockOrder` agents representing daily demand and restock events
- **State Variables:** `inventory`, `dailyDemand`, `fulfilledSales`, `lostSales`, `holdingCost`, `lostSalesCost`, `serviceLevel`, `restocksTriggered`, `restockOrdered`
- **Input Parameters:**
  - `initialStock` = 220
  - `reorderPoint` = 40
  - `restockQuantity` = 400
  - `leadTime` = 2
  - `holdingCostPerUnit` = 1.5
  - `lostSalesCostPerUnit` = 20
  - `simulationDays` = 7

### Process Flow

1. 📅 At the start of each day, demand is generated from deterministic input.
2. ✅ Fulfilled and lost sales are determined based on available inventory.
3. 🔁 When inventory falls below the reorder point (and no restock is active), a restock is placed.
4. 🚚 Restock arrives after a 2-day lead time and replenishes stock.
5. 📊 KPIs (holding cost, lost sales cost, service level) are calculated at the end of each day.

---

## 📈 Results

### Optimized Simulation Run

| Day | Demand | Stock Before Sales | Fulfilled Sales | Lost Sales | Inventory End | Holding Cost ($) | Lost Sales Cost ($) | Service Level (%) | Restock Triggered |
|---|---:|---:|---:|---:|---:|---:|---:|---:|:---:|
| 1 | 46 | 220 | 46 | 0 | 174 | 261 | 0 | 100 | ❌ |
| 2 | 59 | 174 | 59 | 0 | 115 | 172.5 | 0 | 100 | ❌ |
| 3 | 68 | 115 | 68 | 0 | 47 | 70.5 | 0 | 100 | ✅ |
| 4 | 54 | 47 | 47 | 7 | 0 | 0 | 140 | 87.04 | ❌ |
| 5 | 54 | 0 | 0 | 54 | 0 | 0 | 1080 | 0 | ❌ |
| 6 | 47 | 0 | 0 | 0 | 400 | 600 | 0 | 100 | ❌ |
| 7 | 68 | 400 | 68 | 0 | 332 | 498 | 0 | 100 | ❌ |

### 📊 Key Metrics Summary

| Metric | Value |
|---|---:|
| 💰 Total Holding Cost | **$1,602** |
| 📉 Total Lost Sales Cost | **$1,220** |
| 💵 **Total Cost** | **$2,822** |
| 🎯 **Average Service Level** | **84.6%** |

### 🏆 Optimal Parameters Found

| Parameter | Value |
|---|---:|
| Initial Stock | **220 units** |
| Reorder Point | **40 units** |
| Restock Quantity | **400 units** |

> 📈 **Compared to baseline:** the optimized policy improved service level from **45.45% → 84.6%** and reduced total cost from **$4,560 → $2,822**.

---

## 🖼️ Model Visuals

The `Visuals/` folder contains AnyLogic model screenshots across development phases:

- `phase3.PNG` / `phase3run.PNG` — Phase 3 model structure and simulation run
- `phase4.PNG` — Phase 4 model structure with multi-experiment logic
- `phase5run.PNG` / `phase5best.PNG` — Phase 5 simulation run and best-result configuration
- `modelwithvisuals.PNG` — Full model overview with visual components

---

## 💡 Insights

- ⚠️ Stocking late can lead to irrecoverable lost sales — even a high restock quantity can't make up for a delayed trigger.
- 📦 Increasing initial inventory raises holding costs, which can offset the benefits of restocking late.
- 🔁 A higher reorder point (e.g., 40 units) allows replenishment early enough to absorb demand spikes.
- 🧪 Simulating scenarios before committing to inventory levels supports genuinely data-driven decisions.

## ✅ Recommendations

- Use **Initial Stock = 220** and **Restock Quantity = 400** to ensure demand is covered after the initial depletion phase.
- Consider introducing **stochastic demand models** in future simulations to better reflect real-world uncertainty.
- Establish **return or donation policies** for surplus inventory as an ethical disposal method.

## ⚖️ Ethical Considerations

- Overstocking wastes resources — financial and social gains shouldn't come at the expense of environmental responsibility.
- Service level directly affects customer satisfaction; long-term brand loyalty shouldn't be sacrificed for short-term cost-cutting.
- Simulation assumptions should be applied without bias in the decision-making process.

---

## 📝 Conclusion

This project demonstrates how business simulation can solve real operational problems. Using an AnyLogic-based discrete-event model, the team simulated inventory strategy and outcomes under deterministic demand, arriving at a policy that balances cost efficiency with customer service. The final recommended strategy delivers:

- 🎯 A robust service level of **84.6%**
- 💵 Minimized total cost of **$2,822**
- 🔄 A scalable model suited for future experimentation with probabilistic demand

---

## 📁 Project Structure

```text
BA project/
│
├── Phase3_Simulation.alp          # AnyLogic simulation model
├── python_simulation.ipynb        # Supplementary Python-based simulation/analysis
├── Major details.docx             # Project documentation
├── Project-Phase 1_BA.docx        # Phase 1 report
├── Project-Phase 2_BA.docx        # Phase 2 report
├── Project_Phase-2_Data.xlsx      # Phase 2 dataset
│
└── Visuals/
    ├── modelwithvisuals.PNG
    ├── phase3.PNG
    ├── phase3run.PNG
    ├── phase4.PNG
    ├── phase5best.PNG
    └── phase5run.PNG
```

---

## 👥 Team

| Name | Roll Number |
|---|---|
| Hassaan Shahid | 23I-5004 |
| Rayyan Asim | 23I-5002 |
| Sohaib Safdar | 23I-5030 |
| Hussain Asad | 23I-5085 |
| M. Waleed | 23I-5141 |

**Section:** 4B · **Course:** Fundamentals of Business Analytics · **Instructor:** Sir Hammad Majeed
**FAST School of Management, Islamabad — National University of Computer and Emerging Sciences**

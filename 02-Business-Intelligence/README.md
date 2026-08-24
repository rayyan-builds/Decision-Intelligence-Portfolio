<div align="center">

# 🏗️ Horizon Bid Room
### Tender Performance & Business Intelligence Dashboard

**Transforming raw bidding data into a decision-support system for tender strategy, win-rate analysis, and profitability management.**

[![Power BI](https://img.shields.io/badge/Power%20BI-F2C811?style=flat-square&logo=powerbi&logoColor=black)](#)
[![DAX](https://img.shields.io/badge/DAX-217346?style=flat-square&logo=microsoftexcel&logoColor=white)](#)
[![HTML5](https://img.shields.io/badge/HTML5-E34F26?style=flat-square&logo=html5&logoColor=white)](#)
[![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=flat-square&logo=javascript&logoColor=black)](#)
[![Chart.js](https://img.shields.io/badge/Chart.js-FF6384?style=flat-square&logo=chartdotjs&logoColor=white)](#)
[![Status](https://img.shields.io/badge/status-portfolio%20case%20study-blue?style=flat-square)](#)
[![License](https://img.shields.io/badge/license-MIT-lightgrey?style=flat-square)](#license)

</div>

---

## 📌 Overview

**Horizon Bid Room** is a Business Intelligence case study built during a BI internship at **Horizon Tech Services Pvt. Ltd.**, focused on one core question every project-based organization faces:

> *How can tender and bidding data be transformed into a decision-support system that shows management where the organization is winning, where it is losing, how much value is being captured, which markets and business units perform best, and why opportunities are being lost or declined?*

The project was **not** an exercise in dashboard styling. It is an end-to-end analytics workflow — data modelling, KPI engineering, DAX development, and executive reporting — applied to a real tender-performance dataset, delivered in two complementary forms:

| Layer | Purpose |
|---|---|
| 🖥️ **HTML Bid Room** | An interactive, browser-based tender-performance interface for rapid, ad-hoc exploration of bidding data |
| 📊 **Power BI Executive Dashboard** | An enterprise-style BI solution — data model, DAX measures, and a curated executive report built by analysing the HTML interface and re-engineering it as a governed BI asset |

---

## 🎯 Business Problem & Objective

Organizations that bid on projects generate large volumes of tender data — but that data is only valuable if it can answer management's real questions: *are we winning enough, where, at what margin, and why not more often?*

The objective of this project was to design a **tender intelligence layer** that consolidates bidding activity into a single, filterable source of truth, enabling leadership to:

- Monitor the health of the tender pipeline at a glance
- Quantify win-rate performance across markets, industries, and teams
- Track the profitability of won work, not just the volume of it
- Diagnose *why* bids are lost or not pursued, instead of only reporting outcomes
- Hold business units and bid managers accountable with performance scorecards

## ❓ Business Questions Answered

1. How many tenders are in the pipeline, and how many were actually submitted?
2. What is the organization's overall bidding win rate?
3. How much project value has been won?
4. What is the estimated profitability and average profit margin of won projects?
5. How does bidding performance trend over time?
6. Which countries produce stronger win rates?
7. Which industries show stronger bidding performance?
8. Which business units generate the greatest value from won projects?
9. How are individual bid managers performing?
10. Why are opportunities being lost?
11. Why are certain opportunities not being pursued at all?
12. Which individual tender records require further management attention?

---

## 🗂️ Data Overview

The analysis is built on a **tender-level bidding dataset** covering **500 project records** (`P0001`–`P0500`). The dataset used in this repository is a **sanitized, portfolio-safe version** of the internship dataset — client names, values, and identifiers have been generalized/anonymized and do not represent actual Horizon Tech Services production or client data.

<details>
<summary><strong>📋 Key data fields</strong></summary>

| Category | Fields |
|---|---|
| **Identification** | Project ID, Project Name, Client |
| **Segmentation** | Country, Industry, Business Unit, Procurement Method |
| **Bid Lifecycle** | Tender Date, Bid Status, Bid Submitted, Bid Manager |
| **Financials** | Bid Amount, Winning Bid Amount, Project Value, Estimated Cost, Estimated Profit, Profit Margin % |
| **Outcome** | Horizon Result, Winning Company, Competitor, Contract Awarded |
| **Diagnostics** | Reason Not Bid, Reason Lost |
| **Delivery** | Project Duration (Months) |

</details>

**Dataset composition:**

| Metric | Value |
|---|---|
| Total tender records | 500 |
| Bid outcomes tracked | `Won` · `Lost` · `Not Bid` |
| Countries covered | 14 (concentrated across GCC markets, plus a broader international spread) |
| Industries covered | 7 (Aviation, Healthcare, Infrastructure, Energy, Oil & Gas, Commercial, Water) |
| Business units | 4 (Industrial, Civil, Buildings, MEP) |
| Bid managers tracked | 5 |
| Loss/decline reason categories | 4 each for "Reason Lost" and "Reason Not Bid" |

---

## 🧰 Technology Stack

| Layer | Tools |
|---|---|
| **BI & Modelling** | Microsoft Power BI Desktop, DAX, Power Query |
| **Interactive Web Dashboard** | HTML5, CSS3, JavaScript |
| **Charting (Web)** | Chart.js |
| **Data Ingestion (Web)** | XLSX.js (client-side workbook/CSV parsing) |
| **Source Data** | Excel (`.xlsx`) tender-level dataset |

---

## 📐 Analytics & KPI Framework

Every metric was purpose-built to answer a specific management question rather than to decorate a page. Core KPIs engineered across both implementations:

| KPI | Definition | Business Value |
|---|---|---|
| **Total Tenders** | Count of all tender opportunities logged | Pipeline visibility |
| **Submitted Tenders** | Tenders where a bid was actually placed | Bidding activity / capacity utilization |
| **Win Rate** | `Won ÷ (Won + Lost)` | Competitiveness of submitted bids |
| **Value Won** | Sum of project value for won tenders | Revenue capture |
| **Estimated Profit** | Sum of estimated profit on won tenders | Profitability of the won portfolio |
| **Average Profit Margin %** | Mean margin across won projects | Quality (not just volume) of wins |
| **Win Rate by Country / Industry / Business Unit** | Win rate sliced by dimension | Where to focus business development effort |
| **Bid Manager Scorecard** | Won/Lost/Not-Bid split per manager | Individual performance and coaching needs |
| **Reason Lost / Reason Not Bid** | Categorical breakdown of negative outcomes | Root-cause diagnosis, not just outcome reporting |

---

## 🖥️ HTML Bid Room — Interactive Layer

The HTML dashboard is an interactive tender-performance analytics interface designed for fast, hands-on exploration of the bidding portfolio.

**Dashboard sections:**

1. **Portfolio Snapshot** — Total Tenders, Win Rate, Value Won, Average Profit Margin, Estimated Profit
2. **Win Performance** — Bid Status Over Time, Won/Lost/Not-Bid outcome split
3. **Competitive & Market Analysis** — Win Rate by Country, Win Rate by Industry, Value Won by Business Unit
4. **Profitability & Team Performance** — Profit Margin Distribution (won projects), Bid Manager Scorecard
5. **Lost / Declined Analysis** — Why We Lost, Why We Didn't Bid
6. **Tender Register** — A sortable, filterable record-level table (Project ID, Client, Country, Industry, Business Unit, Tender Date, Bid Status, Project Value, Profit Margin %, Bid Manager)

**Interactive capabilities:**

- 🔍 Multi-dimensional filtering — Country, Industry, Business Unit, Bid Status, Bid Manager, Procurement Method
- 🔄 Live filter recalculation across all KPIs and charts
- 📤 Workbook/CSV upload for refreshed data
- 📥 CSV export of the currently filtered tender register
- ↕️ Sortable, paginated tender register table

---

## 📊 Power BI Executive Dashboard

The Power BI report was **not** a direct rebuild of the HTML dashboard — it was engineered as its own governed BI solution, informed by a component-by-component analysis of the HTML interface.

**Process:** the HTML Bid Room was studied to understand its KPI hierarchy, information prioritization, navigation logic, and analytical dimensions. Those concepts were then re-implemented in Power BI using a proper semantic model rather than hard-coded chart logic — meaning KPIs are calculated dynamically via DAX and respond to any slicer combination.

**Work performed:**

- Data modelling of the tender dataset into a Power BI semantic model
- DAX measure development for all core and derived KPIs
- Interactive slicers across Client, Country, Industry, Procurement Method, Business Unit, Bid Manager, and Bid Status
- Executive-style report layout prioritizing decision-relevant KPIs above detail views
- Iterative validation of DAX calculations against source data, refined through review feedback

**Visualizations used:**

`KPI Cards` · `Bar & Column Charts` · `Trend/Line Analysis` · `Treemap` · `Filled Map` · `Scatter Chart` · `Performance Scorecards`

<div align="center">

*Reference view of the HTML Bid Room interface analysed as the basis for the Power BI report:*

`Power_BI_Dashboard.PNG` — see `/screenshots`

</div>

---

## 📈 Key Insights (from the sample dataset)

> Figures below are computed directly from the 500-record portfolio dataset included in this repository and reflected in the Power BI report's KPI cards.

| Metric | Value |
|---|---|
| Total tenders | **500** |
| Submitted tenders | **323** |
| Overall win rate (Won ÷ Submitted) | **52.0%** |
| Total value won | **$12.34bn** |
| Total estimated profit (won projects) | **$2.09bn** |
| Average profit margin (won projects) | **17.68%** |

**Notable patterns surfaced by the analysis:**

- Bidding activity is concentrated in **GCC markets** (Qatar, Kuwait, Saudi Arabia, Bahrain, UAE, Oman), with a smaller, evenly-distributed footprint across international markets (Pakistan, India, Europe, South America).
- **Aviation, Healthcare, and Infrastructure** are the highest-volume industries by tender count, ahead of Energy, Oil & Gas, Commercial, and Water.
- Business unit activity is fairly balanced (Industrial, Civil, Buildings, MEP), which the dashboard uses to compare **value won**, not just volume, across units.
- **Lower technical score** and **higher price** are the two leading causes of lost bids — pointing management toward technical-proposal quality and pricing strategy as priority levers.
- **"Out of scope"** and **"budget limits"** are the leading reasons opportunities are not pursued at all — useful for evaluating whether the current opportunity pipeline is well-matched to organizational capability.

---

## 🔁 Project Workflow

```
Raw / structured bidding data
            ↓
Data understanding & modelling
            ↓
KPI engineering with DAX
            ↓
Interactive analytical layer (HTML)
            ↓
Power BI executive reporting
            ↓
Business performance insights
            ↓
Better tender and bidding decisions
```

---

## 📁 Repository Structure

```
horizon-bid-room/
│
├── README.md                                          # Project documentation (this file)
├── data/
│   └── Project_Bidding_dataset.xlsx                   # Sanitized tender-level dataset (500 records)
│
├── powerbi/
│   ├── Project_bidding_Horizon.pbix                   # Power BI report — data model + DAX + visuals
│   └── project_bidding_dashboard_draft.pbix            # Earlier working draft of the report
│
├── html-bid-room/
│   └── index.html                                     # Interactive HTML/JS Bid Room dashboard
│
└── screenshots/
    └── Power_BI_Dashboard.PNG                          # Dashboard reference screenshot
```

---

## ⚙️ Technical Implementation Notes

- **Data modelling:** the tender dataset was loaded into Power BI's semantic model, with categorical fields (Country, Industry, Business Unit, Bid Status, Procurement Method, Bid Manager) modelled as filterable dimensions.
- **DAX measures** were written for every headline KPI (Total Tenders, Submitted Tenders, Win Rate, Value Won, Estimated Profit, Average Profit Margin) so they recalculate correctly under any combination of slicers, rather than being pre-aggregated.
- **Win-rate logic** is calculated as Won ÷ (Won + Lost), deliberately excluding "Not Bid" records from the denominator to reflect competitive performance only on tenders actually contested.
- **The HTML layer** parses uploaded workbook/CSV data client-side via XLSX.js and renders all charts with Chart.js, recalculating every KPI and visual on each filter change without a server round-trip.
- **Calculations were validated** by cross-checking Power BI KPI card outputs against manual aggregation of the source dataset.

---

## 💼 Business Value

This project demonstrates how a bidding function can move from **reactive tender logging** to **proactive performance management**:

- Leadership gets a single, trustworthy view of pipeline health and win performance instead of scattered spreadsheets
- Profitability — not just win count — becomes a visible, trackable metric
- Loss and decline reasons are quantified, turning anecdotal explanations into a diagnosable pattern
- Country, industry, and business-unit views support **where to invest business development effort next**
- Bid manager scorecards support **individual performance conversations** with objective data

---

## ⚠️ Limitations & Assumptions

- The dataset published in this repository is a **sanitized, portfolio-safe sample** and does not represent live or production data from Horizon Tech Services.
- The dashboards reflect a **static snapshot** of tender data; there is no live/real-time connection to an organizational tendering system.
- No machine learning or predictive modelling is used — all analysis is descriptive/diagnostic BI (KPIs, trends, breakdowns), consistent with the project's actual scope.
- The HTML Bid Room is a standalone client-side interface intended for portfolio demonstration, not a deployed enterprise application.

---

## 🚀 Future Improvements

- Automate data refresh via a scheduled Power BI dataflow or gateway connection
- Add predictive win-probability scoring based on historical bid characteristics
- Extend the Bid Manager Scorecard with time-to-submission and cycle-time metrics
- Introduce row-level security in Power BI for business-unit-restricted views
- Add a drill-through page from the Tender Register to a single-tender detail view

---

## 🧠 Skills Demonstrated

`Business Intelligence` · `Data Modelling` · `DAX` · `KPI Engineering` · `Power BI Report Design` · `Data Analysis` · `Dashboard/UX Translation (HTML → Power BI)` · `JavaScript/Chart.js Development` · `Business Performance Reporting` · `Stakeholder-Focused Analytics`

---

<div align="center">

**Project completed as part of a Business Intelligence internship at Horizon Tech Services Pvt. Ltd.**

*This repository is shared as a portfolio case study using sanitized, non-confidential data.*

</div>

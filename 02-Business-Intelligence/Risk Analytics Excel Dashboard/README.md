# 🛡️ Risk Analytics Dashboard

### Enterprise Risk Management & Business Intelligence — Excel, Data Analytics & Decision Support

**Risk Analytics Dashboard** is an Excel-based risk management and analytics solution built to support an organization's **ISO/IEC 27001:2022 and ISO 9001:2015** compliance programme. It converts a structured risk register into a live, formula-driven analytical system — scoring risks consistently, tracking treatment progress, and surfacing residual exposure through an executive dashboard, without relying on PivotTables, macros, or external refresh steps.

Rather than functioning as a static administrative log, the workbook operates as a self-contained **risk intelligence engine**: every risk entered into the register is automatically scored, banded, ranked, and reflected in real time across a `SUMIFS`/`COUNTIFS`-driven data layer and a filterable executive dashboard. The result is a single workbook that supports both the operational task of documenting risk and the management task of monitoring it.

This project demonstrates core Business Intelligence competencies — structured data modelling, rule-based scoring logic, KPI design, and executive-level dashboard construction — applied to a governance, risk, and compliance (GRC) use case grounded in recognised ISO standards.

---

## 🎯 Project Overview

Organizations pursuing ISO 27001 and ISO 9001 certification are required to maintain a documented, defensible risk assessment process — one that identifies risks, scores them consistently, tracks how they are treated, and demonstrates that residual exposure has been reduced to an acceptable level. Doing this in an ad-hoc or purely descriptive spreadsheet makes it difficult to prioritise action or prove control effectiveness to auditors and management.

This workbook addresses that by building the risk register and its analytics into the **same structure**:

- Every risk is scored using a governed, parameter-driven formula rather than subjective judgement
- Risk banding (`HIGH` / `MEDIUM` / `LOW`) is derived automatically from those scores
- Treatment actions and their effectiveness are tracked through to a **post-treatment (residual) risk assessment**
- All of this feeds a live executive dashboard, so the workbook functions as an ongoing monitoring tool rather than a one-time assessment document

What makes this an analytics/BI solution rather than a plain risk register is the **calculation engine**: a dedicated `Dashboard Data` sheet aggregates the register with `SUMIFS`/`COUNTIFS` formulas, a hidden ranking column drives a "Top 5 risks" view, and every KPI and chart on the dashboard recalculates instantly as register data changes — with no manual refresh step.

---

## 🏢 Business Problem

Compliance and risk-management functions commonly struggle with:

- **Inconsistent risk scoring** — different assessors rating the same risk differently, undermining comparability
- **Difficulty prioritising** — a long list of risks with no clear ranking of what needs attention first
- **Limited visibility into treatment effectiveness** — knowing a control was *implemented* is not the same as knowing it *reduced risk*
- **No consolidated view for management** — risk detail sitting in a register that executives don't have time to read line by line
- **Manual, error-prone recalculation** — spreadsheets that break or require rebuilding every time a new risk is added

This workbook is designed to remove those failure points: risk scoring is rule-based and parameter-driven (not free-text judgement), every calculated column is blank-safe so incomplete rows can't break downstream formulas, and the dashboard requires no refresh because it reads live from the register.

---

## 🔄 Solution Workflow

```text
Risk Identification
        ↓
Risk & Asset Assessment  (Confidentiality × Integrity × Availability)
        ↓
Risk Scoring & Banding  (Asset Criticality × Likelihood × Consequence)
        ↓
Risk Treatment Planning  (Action, Owner, Timescale, Status)
        ↓
Post-Treatment / Residual Assessment
        ↓
Live Dashboard Data Engine  (SUMIFS / COUNTIFS)
        ↓
Executive Dashboard  (KPIs, Charts, Filters)
        ↓
Management Decision Support & ISO 27001/9001 Reporting
```

---

## 📊 Dashboard & Analytics

The workbook's **Executive Dashboard** is described in its own documentation as a client-facing, one-page view — read-only in practice, aside from its two filter controls.

**KPI cards on the dashboard:**

| KPI | Purpose |
|---|---|
| Total Risks Identified | Overall size of the risk population |
| High Residual Risks | Risks still rated HIGH *after* treatment |
| Medium Residual Risks | Risks still rated MEDIUM after treatment |
| Low Residual Risks | Risks reduced to LOW after treatment |
| Risk Reduction | Overall percentage reduction in risk score achieved through treatment |
| Open Treatment Actions | Treatment actions not yet started |
| Overdue Actions | Treatment actions past their due timescale (calculated using `TODAY()`) |
| Closed Treatment Actions | Treatment actions completed |

**Charts:**

1. **Risk Exposure by Asset Category — Inherent vs Residual** (clustered bar) — compares pre-treatment and post-treatment exposure across each Asset Category
2. **Top 5 Residual Risks — Highest Remaining Exposure** (bar) — ranks the five risks with the greatest remaining exposure after treatment, driven by a hidden `Dash Rank` helper column in the register
3. **Treatment Delivery by Accountable Owner** (stacked bar) — shows each owner's caseload split across `Pending`, `Open`, and `Close` status

**Filters:**

- **Asset Category** — isolate KPIs and charts to a single asset category (or view all)
- **Treatment Action Status** — isolate KPIs and charts to a specific treatment status (or view all)

Both filters drive every KPI and chart on the page simultaneously, allowing a manager to, for example, view residual exposure for only the `Infrastructure` category or only `Open` treatment actions.

Using these views, a manager can identify which asset categories carry the most residual exposure, which owners are carrying the heaviest treatment workload, which specific risks remain the greatest concern after mitigation, and whether any treatment actions are overdue.

---

## ⚠️ Risk Assessment Framework

The workbook uses a defined, parameter-driven scoring methodology (documented on its `Introduction` sheet):

**Step 1 — Asset Value**
```
Asset Value = C × I × A
```
Confidentiality (`C`), Integrity (`I`), and Availability (`A`) are each rated 1–3, giving an Asset Value range of 1–27.

**Step 2 — Asset Criticality / Rating**
```
Asset Criticality = 1   if Asset Value ≤ 6
                   = 2   if Asset Value ≤ 12
                   = 3   otherwise
```

**Step 3 — Risk Score**
```
Risk Score = Asset Criticality × Likelihood Score × Consequence Score
```
This produces a score from 1–27. Likelihood and Consequence are **ordered lookup lists** on the `Lookup Lists` sheet (e.g. Likelihood: `Rare → Likely → Almost Certain`), where a value's position in the list *is* its numeric score — looked up via `MATCH` rather than nested `IF` statements.

**Step 4 — Risk Level / Banding**
```
Risk Level = HIGH    if score ≥ 18
           = MEDIUM  if score ≥ 7
           = LOW     otherwise
```
These thresholds (18 and 7) are **governed parameter cells** on the `Lookup Lists` sheet, not hard-coded into formulas — changing them re-bands the entire register instantly.

**Post-Treatment (Residual) Assessment:** the same formula is re-applied using a re-assessed Likelihood and Consequence *after* the treatment action, producing a **Post-Treatment Risk Score** and **Post-Treatment Risk Level** for every risk — the workbook's mechanism for measuring residual risk rather than only inherent risk.

**Review scheduling:** the `Next Review Date` is calculated as the treatment date plus **3, 6, or 12 months**, depending on the residual risk level, referencing ISO 27001 Clause 8.2 — with the review intervals themselves stored as governed parameters on `Lookup Lists` rather than hard-coded.

---

## 🛠️ Risk Treatment & Monitoring

For each risk, the register captures:

- **Treatment Option Chosen** — e.g. `Modify` (the only option used across the current dataset), from a governed list that also includes `Avoid`, `Accept`, and `Share`
- **Proposed Treatment Action** — the specific control or mitigation implemented
- **Annex A / Control Reference** — the corresponding ISO 27001 Annex A control and/or ISO 9001 clause the action satisfies
- **Treatment Action Owner** — the accountable role responsible for delivery
- **Treatment Action Timescale** — a true date field (converted from text in v1.1) enabling overdue tracking
- **Treatment Action Status** — `Pending`, `Open`, or `Close`

Post-treatment monitoring is supported through the **Post-Treatment Assessment** block — a re-assessed Likelihood, Consequence, Asset Value, Risk Score, and Risk Level for each risk — and through the dashboard's **Overdue Actions** KPI, which ages automatically using `TODAY()` rather than requiring manual review.

---

## 🗂️ Workbook Structure

| Sheet | Purpose |
|---|---|
| `Introduction` | Document control, workbook usage guide, risk scoring methodology, and version change log |
| `Risk Register` | The single source of truth — one row per risk, spanning identification, assessment, treatment, and post-treatment/residual assessment |
| `Dashboard Data` | The live calculation engine — `SUMIFS`/`COUNTIFS` formulas aggregating the register into the exact data blocks each dashboard chart reads from |
| `Executive Dashboard` | The one-page, filterable management view — KPI cards, charts, and slicers |
| `Lookup Lists` | Governed dropdown source lists (Asset Category, Likelihood, Consequence, Treatment Status, Treatment Option, Owner) plus the yellow-highlighted risk-scoring parameter cells (thresholds, review intervals) |

---

## 📋 Key Data Fields

### Risk Identification
- Ref
- Asset Category
- Domain
- Asset
- Asset Description
- Risk Description
- Risk Type
- Vulnerability

### Asset & Risk Assessment
- Confidentiality (C) / Integrity (I) / Availability (A)
- Asset Value
- Asset Criticality / Rating
- Asset Evaluation
- Risk Owner
- Likelihood / Likelihood Score / Likelihood Rationale
- Consequences / Consequence Score / Consequences Rationale
- Risk Score
- Risk Value (Risk Level)

### Risk Treatment
- Treatment Option Chosen
- Proposed Treatment Action
- Annex A / Control (ISO 27001 & ISO 9001)
- Treatment Action Owner
- Treatment Action Timescale
- Treatment Action Status

### Post-Treatment / Residual Risk
- Post Treatment Asset Value
- Post-Treatment Likelihood / Likelihood Score
- Post-Treatment Consequences / Consequence Score
- Post-Treatment Risk Score
- Post-Treatment Risk Level

### Dashboard Support
- Comments
- Dash Rank *(hidden helper column driving the Top 5 residual risk chart)*

---

## 📈 Key Results & Business Insights

The figures below are read directly from the workbook's Executive Dashboard and Risk Register (10 logged risks, all filters set to "All"):

| Metric | Result |
|---|---:|
| Total Risks Identified | **10** |
| High-Rated Risks (inherent) | **3** |
| Medium-Rated Risks (inherent) | **7** |
| High Residual Risks (post-treatment) | **0** |
| Medium Residual Risks (post-treatment) | **0** |
| Low Residual Risks (post-treatment) | **10** |
| Overall Risk Reduction | **≈ 67.2%** |
| Closed Treatment Actions | **10** |
| Open Treatment Actions | **0** |
| Overdue Actions | **0** |

**What this means from a management perspective:**

- Every risk currently logged in the register has an associated treatment action that has been **closed**, and every risk's residual rating has been reduced to **LOW** — the dashboard shows a fully treated risk population as of the current snapshot, with an average risk-score reduction of roughly two-thirds.
- Inherent risk before treatment was concentrated at **MEDIUM** (7 of 10 risks) and **HIGH** (3 of 10 risks — all within `Infrastructure` and `Software and Application`), which is where treatment effort was correspondingly focused.
- By **Asset Category**, `Infrastructure` (3 risks) and `Documentation (GRC)` (3 risks) carry the most entries, followed by `HR` (2), and single entries each for `Software and Application` and `Miscellaneous`.
- **Treatment ownership** is concentrated with the `IT Head` (4 risks) and `HR Manager` (3 risks), with `Development Lead`, `Compliance Consultant`, and `Operations Team` each owning one — visible directly on the "Treatment Delivery by Accountable Owner" chart.
- Because the dashboard is live and filterable, this snapshot will change automatically as new risks are added or existing ones re-assessed — it is a monitoring tool, not a one-time report.

---

## 💼 Business Questions Answered

1. **How many risks has the organization identified, and how are they distributed?** — The `Total Risks Identified` KPI and the "Risk Exposure by Asset Category" chart answer this instantly, filterable by category.
2. **Which risks carry the greatest residual exposure after treatment?** — The "Top 5 Residual Risks" chart, ranked via the hidden `Dash Rank` column, surfaces this directly.
3. **How effective has risk treatment been?** — The `Risk Reduction` KPI quantifies the average reduction in risk score achieved through the treatment programme.
4. **Are any treatment actions overdue?** — The `Overdue Actions` KPI, driven by `TODAY()` against the Treatment Action Timescale, flags this without manual checking.
5. **How is treatment workload distributed across the organization?** — The "Treatment Delivery by Accountable Owner" chart shows each owner's `Pending`/`Open`/`Close` breakdown.
6. **Which asset categories carry the most inherent vs residual exposure?** — The clustered "Inherent vs Residual" chart directly compares pre- and post-treatment exposure per category.
7. **What is the current risk-level distribution — how many High, Medium, and Low risks remain?** — The `High/Medium/Low Residual Risks` KPI cards give this at a glance.

---

## 🧠 Business Intelligence Value

Although delivered in Excel, this project demonstrates core BI and analytics practices:

- **Structured data modelling** — a single, well-defined risk register table (`tblRiskRegister`) acting as the sole source of truth for every downstream calculation
- **Rule-based, parameter-driven scoring** — risk thresholds and review intervals stored as governed parameter cells rather than hard-coded into formulas, so business rules can change without touching logic
- **Data validation and governance** — all categorical fields (Asset Category, Likelihood, Consequence, Owner, Status) are drawn from a single governed `Lookup Lists` sheet, ensuring consistency and preventing free-text drift
- **KPI design** — eight distinct, decision-relevant KPIs derived from raw register data via live aggregation formulas
- **A live calculation/aggregation layer** — the `Dashboard Data` sheet functions as a formula-based "semantic layer," using `SUMIFS`/`COUNTIFS` to pre-shape data specifically for each chart, separate from the raw register
- **Dashboard and executive reporting design** — a single, filterable, decision-oriented page rather than a raw data dump
- **Defensive/error-safe design** — every calculated column is blank-safe, so a partially completed row cannot break the dashboard, a meaningful analytics-engineering consideration beyond just "using formulas"

---

## 🧩 Technology & Tools

| Technology | Purpose |
|---|---|
| Microsoft Excel | Risk data management, calculation engine, and dashboard |
| Excel formulas (`SUMIFS`, `COUNTIFS`, `MATCH`, `TODAY()`) | Risk scoring, live KPI aggregation, and overdue/review-date logic |
| Excel Tables & Data Validation | Governed dropdown lists and self-extending risk register |
| Excel Charts (bar / stacked bar) | Dashboard visualization |
| Excel slicers/filters | Interactive, dashboard-wide filtering by Asset Category and Treatment Status |

---

## 🏗️ Project Architecture

```text
Risk Register Data  (tblRiskRegister)
        │
        ▼
Data Validation & Governed Reference Lists  (Lookup Lists)
        │
        ▼
Risk Assessment & Scoring  (C × I × A → Asset Criticality × Likelihood × Consequence)
        │
        ▼
Risk Treatment  (Action, Owner, Timescale, Status)
        │
        ▼
Post-Treatment / Residual Risk Assessment
        │
        ▼
Live Aggregation Engine  (Dashboard Data — SUMIFS / COUNTIFS)
        │
        ▼
Executive Dashboard  (KPI Cards, Charts, Filters)
        │
        ▼
Management Decision Support & ISO 27001 / ISO 9001 Reporting
```

---

## ⚠️ Limitations & Assumptions

- The workbook contains **10 logged risk records** at the time of this snapshot — a real production register would typically be larger; the analytics logic scales with the register but the current dataset size limits statistical generality.
- All 10 risks in the current dataset use the `Modify` treatment option and are `Closed` with `LOW` residual risk — the dashboard supports `Avoid`, `Accept`, and `Share` treatment options and `Pending`/`Open` statuses, but no examples of these currently exist in the data.
- Overdue and review-date logic depends on `TODAY()`, so KPI values such as `Overdue Actions` will change simply with the passage of time, independent of any data entry.
- This is a **single-workbook, single-user-at-a-time** solution (no database backend or multi-user concurrency handling); it is well suited to a compliance team's internal register but not designed as a multi-user enterprise system.
- Some organizational details in the workbook (client name, document numbers) are specific to the originating engagement and have been retained here only where non-sensitive/structural, consistent with a portfolio case-study use.

---

## 🧾 About This Workbook

This workbook was built and iterated in a governed, versioned way — its `Introduction` sheet documents a formal change record (v1.0 → v1.1) including standardising categories, converting text dates to true dates to enable overdue logic, replacing nested `IF` chains with `MATCH`-based lookups, and adding blank-safe handling across every calculated column. This version-controlled approach to a "living" analytical workbook — rather than a one-off spreadsheet — is itself part of what makes it a Business Intelligence deliverable rather than a static document.

---

<div align="center">

**Confidential structural details have been generalized for portfolio presentation.**
**Sample data reflects a compliance-programme risk register built to ISO/IEC 27001:2022 and ISO 9001:2015 requirements.**

</div>

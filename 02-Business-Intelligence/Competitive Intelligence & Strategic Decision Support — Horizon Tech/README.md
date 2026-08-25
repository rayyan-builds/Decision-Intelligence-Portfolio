# Competitive Intelligence & Strategic Decision Support — Horizon Tech

### An interactive strategy command center translating competitor benchmarking, gap analysis, and roadmap data into a decision-support tool for cybersecurity market positioning.

---

## 📌 Overview

This project was developed as part of Business Intelligence work at **Horizon Tech Services Pvt. Ltd.**, a cybersecurity company positioning itself against established competitors in the endpoint detection and managed security services market.

Rather than presenting competitor and strategy data as static slides or spreadsheets, this project consolidates it into a single **interactive strategy command center** — a structured, multi-page HTML dashboard backed by a modeled Excel dataset — so leadership can move between competitive positioning, capability gaps, strategic priorities, and execution roadmap in one place.

---

## 🎯 Business Problem

Cybersecurity is a fast-moving, capability-driven market. Leadership needed a clear, structured view of:

- Where Horizon stands relative to direct and indirect competitors
- Which capability gaps are most urgent to close (particularly against category leaders like CrowdStrike)
- What strategic initiatives are underway, and how complete they are
- What needs to happen immediately vs. in later phases
- Which certifications, regions, and talent domains are required to execute the strategy

Without a consolidated view, this kind of strategic intelligence tends to live in disconnected documents — making it hard to track progress or prioritize investment.

---

## 🧭 Solution

A **Strategic Intelligence dataset** (Excel, 11 structured sheets) was modeled to capture every dimension of the strategy — competitors, initiatives, gaps, action items, priorities, certifications, roadmap, regional expansion, talent needs, and platform modules.

This data was then built into the **Horizon Strategy Command Center** — an interactive HTML/CSS/JavaScript dashboard organized into navigable pages, allowing the underlying strategic data to be explored the way an executive would move through a briefing: overview → competitive comparison → AI readiness → priorities → roadmap → talent → platform.

```text
Structured Strategic Data (Excel)
        ↓
Data Modeling Across 11 Dimensions
        ↓
Interactive Command Center (HTML/CSS/JS)
        ↓
Competitive & Strategic Insight
        ↓
Prioritized Decision-Making
```

---

## 🗂️ Data Structure

The underlying dataset (`Horizon_Strategic_Intelligence_Data.xlsx`) is organized into 11 sheets:

| Sheet | Captures |
|---|---|
| **Competitor Info** | Scored benchmarking of Horizon vs. direct/indirect competitors across employee strength, marketing, cybersecurity, product, government relations, and partnerships |
| **Strategies** | Named strategic initiatives, status, and completion percentage |
| **Comparison** | Capability gap analysis against a category-leading competitor, by area and gap severity |
| **AI Checklist** | Readiness tasks for building AI/ML-driven security capabilities |
| **Action Items** | Execution tasks grouped by phase (e.g. immediate 0–3 months) |
| **Priorities** | Ranked strategic priorities with impact rating |
| **Certifications** | Compliance/certification status (achieved, in audit, planned) |
| **Roadmap** | Quarterly phases with deliverables and status |
| **Regions** | Target geographic expansion and current status |
| **Talent** | Key hiring domains and their strategic focus |
| **Platform Modules** | Planned product/platform capabilities and development status |

---

## 🧩 Competitive Benchmarking

The **Competitor Info** sheet scores Horizon against direct and indirect competitors across six weighted dimensions (employee strength, marketing, cybersecurity capability, product maturity, government relationships, and partnerships), rolling up into an **Overall Competitiveness** score. This gives leadership a single comparable figure per competitor rather than six disconnected ratings.

The **Comparison** sheet extends this into a targeted **gap analysis** against a category-leading competitor, area by area (e.g. AI, platform architecture, threat intelligence, cloud security), each tagged with a gap severity (High/Medium) and the corresponding action Horizon needs to take to close it.

---

## 🚦 Strategic Priorities & Roadmap

- **Priorities** are ranked (P1, P2, P3…) with a description and impact rating, giving a clear order of what matters most — e.g. building the core platform before layering on downstream capabilities.
- **Action Items** are grouped by execution phase (starting with an immediate 0–3 month horizon), so near-term tasks are distinguishable from longer-term initiatives.
- **Roadmap** breaks the strategy into quarters, each with a phase name, status (done / current / planned), and concrete deliverables — giving a timeline view of execution progress.
- **Certifications** tracks compliance milestones (e.g. ISO 27001, SOC 2 Type II, PCI DSS, FedRAMP) by status, which matters directly for market credibility and enterprise/government sales eligibility.

---

## 🖥️ Interactive Command Center

`horizon_strategy.html` implements the **Horizon Strategy Command Center** — a self-contained, browser-based dashboard with dedicated pages for:

- **Dashboard** — high-level strategic overview
- **Compare** — competitor and capability-gap comparison
- **AI** — AI/ML readiness overview
- **Checklist** — AI capability build-out checklist
- **Priorities** — ranked strategic priorities
- **Roadmap** — quarterly execution timeline
- **Strategies** — active strategic initiatives and completion tracking
- **Talent** — hiring domains and focus areas
- **Platform** — platform module development status
- **Global** — regional expansion status

The interface is built with plain HTML, CSS, and JavaScript — no external BI tool required to view it — making the strategic data portable and easy to share internally.

---

## 🛠️ Technology Stack

| Area | Tools |
|---|---|
| Data Modeling | Microsoft Excel (multi-sheet structured dataset) |
| Interactive Dashboard | HTML, CSS, JavaScript |
| Analytical Approach | Competitive benchmarking, gap analysis, roadmap/status tracking |
| Domain | Business Intelligence, Competitive Intelligence, Strategic Planning |

---

## 📁 Repository Structure

```text
Competitive Intelligence & Strategic Decision Support — Horizon Tech/
│
├── Horizon_Strategic_Intelligence_Data.xlsx   # 11-sheet strategic intelligence dataset
├── horizon_strategy.html                       # Interactive Strategy Command Center
└── README.md
```

---

## 💼 Business Value

- Converts scattered competitive and strategic information into a **single structured, navigable source of truth**.
- Makes **capability gaps explicit and prioritized**, rather than implicit or anecdotal.
- Links strategic initiatives to a **quarterly roadmap with visible completion status**, supporting accountability.
- Surfaces **certification and regional expansion status** alongside strategy — connecting go-to-market readiness to execution progress.
- Presents strategic intelligence in a format non-technical leadership can explore directly, without needing a BI tool license.

---

## ⚠️ Confidentiality Note

This repository is shared as a **portfolio artifact** demonstrating data modeling and decision-support dashboard design. Company names, competitor references, and figures reflect the internal strategic planning exercise this project was built around and are presented here for illustrative and professional-portfolio purposes rather than as disclosed production business intelligence.

---

## 🧠 Skills Demonstrated

- Multi-dimensional data modeling for strategic/competitive intelligence
- Competitive benchmarking and capability gap analysis design
- Translating strategic planning data into an interactive decision-support interface
- Front-end dashboard development (HTML/CSS/JavaScript) as a lightweight alternative to a full BI platform
- Structuring roadmap, priority, and action-item data for executive-level consumption

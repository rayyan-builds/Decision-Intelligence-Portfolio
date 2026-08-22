<div align="center">

# 🛒 Retail Sales ETL & Database Analytics Pipeline

### 📊 Database Systems for Business — MySQL, SQL, Python & Pandas

[![MySQL](https://img.shields.io/badge/Database-MySQL-4479A1?logo=mysql&logoColor=white)](#-technology-stack)
[![SQL](https://img.shields.io/badge/Language-SQL-CC2927?logo=microsoftsqlserver&logoColor=white)](#-technology-stack)
[![Python](https://img.shields.io/badge/Language-Python-3776AB?logo=python&logoColor=white)](#-technology-stack)
[![Pandas](https://img.shields.io/badge/Library-Pandas-150458?logo=pandas&logoColor=white)](#-technology-stack)
[![Status](https://img.shields.io/badge/Status-Completed-success)](#-project-at-a-glance)

An end-to-end retail data engineering and analytics project that transforms **5,000 raw retail transactions** into a structured relational database and uses SQL-driven business intelligence queries to answer revenue, customer, sales-trend, product, and profitability questions.

</div>

---

## 📑 Table of Contents

- [🧭 Project Overview](#-project-overview)
- [🎯 Project Objectives](#-project-objectives)
- [🛠️ Technology Stack](#️-technology-stack)
- [🗃️ Dataset & Data Pipeline](#️-dataset--data-pipeline)
  - [📂 Dataset Categories & Dimensions](#-dataset-categories--dimensions)
  - [📋 Source Dataset Columns](#-source-dataset-columns)
  - [🧱 Dataset Structure](#-dataset-structure)
- [📈 Project at a Glance](#-project-at-a-glance)
- [🏗️ Final Database Structure](#️-final-database-structure)

---

## 🧭 Project Overview

The project combines **ETL, data cleaning, relational database design, SQL analytics, and Python/Pandas-based data processing** to demonstrate how raw transactional data can be converted into reliable information for business decision-making.

The original **Superstore dataset** contained **5,000 raw retail transaction records** with customer, order, product, sales, quantity, discount, profit, shipping, and geographic information.

### 🔄 ETL Workflow

> **Raw Retail Data → Cleaning & Validation → Staging Table → Relational Database → SQL Analytics → Business Insights**

The transactional data was transformed into a normalized relational structure consisting of:

| 🧩 Table | Description |
|---|---|
| 👤 `Customers` | Customer records |
| 📦 `Products` | Product catalog |
| 🧾 `Orders` | Order-level records |
| 📃 `Order_Details` | Line-item transaction details |

Primary keys and foreign-key relationships were implemented to establish relationships between customers, orders, products, and transaction details.

The SQL workflow also addresses data-quality issues encountered during migration, including duplicate order-product combinations, inconsistent product naming, and repeated customer/order records.

---

## 🎯 Project Objectives

- ✅ Transform raw retail transaction data into a structured relational database
- ✅ Apply ETL and data-cleaning principles to improve data quality
- ✅ Design a normalized relational database structure
- ✅ Establish primary-key and foreign-key relationships
- ✅ Use SQL to perform business-oriented analytical queries
- ✅ Identify revenue, customer, product, sales-trend, and profitability insights
- ✅ Produce reproducible HTML outputs for database validation and analytical results

---

## 🛠️ Technology Stack

| Area | Tools |
|---|---|
| 🗄️ Database | **MySQL** |
| 📝 Primary Analytics Language | **SQL** |
| 🐍 Data Processing | **Python, Pandas** |
| 📄 Data Format | CSV |
| 🔧 ETL | SQL + Python/Pandas |
| 🏛️ Database Design | Relational Database / 3NF principles |
| 📤 Outputs | HTML query-result files |

---

## 🗃️ Dataset & Data Pipeline

The source dataset is a **retail/superstore transactional dataset** containing individual order-line records. It combines information about customers, orders, products, sales performance, profitability, shipping, and geographic markets.

<div align="center">

### 📦 5,000 raw retail transaction records

</div>

The dataset provides both **categorical dimensions** for segmentation and analysis and **numerical measures** for evaluating sales and business performance.

### 📂 Dataset Categories & Dimensions

| Dimension | Fields |
|---|---|
| 👤 **Customer** | Customer name, customer segment |
| 🧾 **Order** | Order ID, order date, ship date, ship mode, order priority |
| 📦 **Product** | Product ID, product name, category, sub-category |
| 🌍 **Geography** | State, country, market, region |
| 💰 **Performance** | Sales, quantity, discount, profit, shipping cost |
| 🕒 **Time** | Order year, order date, ship date |

### 📋 Source Dataset Columns

The original staging dataset contains the following columns:

| Column | Description |
|---|---|
| `order_id` | Unique identifier associated with an order |
| `order_date` | Date on which the order was placed |
| `ship_date` | Date on which the order was shipped |
| `ship_mode` | Shipping method used for the order |
| `customer_name` | Customer associated with the transaction |
| `segment` | Customer segment |
| `state` | State associated with the transaction |
| `country` | Country associated with the transaction |
| `market` | Geographic market |
| `region` | Geographic region |
| `product_id` | Product identifier |
| `category` | Main product category |
| `sub_category` | Product sub-category |
| `product_name` | Name of the product |
| `sales` | Sales/revenue generated by the transaction |
| `quantity` | Number of units sold |
| `discount` | Discount applied to the transaction |
| `profit` | Profit generated by the transaction |
| `shipping_cost` | Cost associated with shipping |
| `order_priority` | Priority assigned to the order |
| `year` | Year associated with the transaction |

> 💡 These fields allow the dataset to support analysis across several business perspectives, including **customer purchasing behavior, product demand, revenue generation, sales patterns, geographic performance, shipping, and profitability**.

### 🧱 Dataset Structure

The source data contains a combination of:

<table>
<tr>
<td valign="top" width="50%">

**🆔 Identifiers**
- Order ID
- Product ID

**🕒 Dates & Time**
- Order Date
- Ship Date
- Year

**👤 Customer & Market Dimensions**
- Customer Name
- Segment
- State
- Country
- Market
- Region

</td>
<td valign="top" width="50%">

**📦 Product Dimensions**
- Product Name
- Category
- Sub-Category

**💰 Business Measures**
- Sales
- Quantity
- Discount
- Profit
- Shipping Cost

**⚙️ Operational Attributes**
- Ship Mode
- Order Priority

</td>
</tr>
</table>

After loading the data into the staging layer, the SQL pipeline transformed it into four related tables.

---

## 📈 Project at a Glance

<div align="center">

| Metric | Result |
|---|---:|
| 📥 Raw/Staging Records | **5,000** |
| 👤 Customers Created | **3,571** |
| 📦 Products Created | **3,798** |
| 🧾 Orders Created | **3,624** |
| 📃 Order Details | **4,997** |
| 🧹 Duplicate Order-Product Pairs Resolved | **3** |
| ❓ Business Questions Answered | **5** |
| 💵 2014 Revenue Identified | **$262,880.28** |
| 📅 Highest Monthly Sales | **$106,158.62 — March** |
| 🏆 Highest-Value Customer | **$4,675.00** |
| 📦 Highest Product Quantity | **79 units** |
| 💻 Most Profitable Category | **Technology — $61,647.01** |

</div>

---

## 🏗️ Final Database Structure

```text
Customers
    │
    └── Orders
            │
            └── Order_Details
                    │
                    └── Products
```

<div align="center">

---

⭐ **A complete ETL-to-Insights pipeline — from raw retail data to actionable business intelligence.** ⭐

</div>

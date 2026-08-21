# 🛒 Retail Sales ETL & Database Analytics

> **Turning raw retail transaction data into a structured SQL analytics system for revenue, customer, product, sales-trend, and profitability analysis.**

**Database Systems for Business**  
*MySQL · SQL · Python · Pandas · ETL · Relational Database Design · Business Analytics*

---

## 📌 Project Overview

This project develops an end-to-end **ETL and relational database analytics pipeline** using a modified Superstore retail dataset containing **5,000 transaction records**.

The objective was to transform a flat, difficult-to-analyze dataset into a structured **3NF relational database**, then use SQL to answer practical business questions around revenue, customers, sales trends, products, and profitability.

The project combines **Python/Pandas for data preparation and ETL** with **MySQL/SQL for database design, data migration, validation, and business intelligence analysis**.

The final pipeline demonstrates how raw transactional data can be converted into a reliable analytical foundation for business decision-making.

---

## 🎯 Business Objective

The project was designed to answer five core business questions:

1. **How much revenue was generated in 2014?**
2. **Which customers generated the highest purchase volumes?**
3. **How do sales vary across months?**
4. **Which products have the highest quantities sold?**
5. **Which product categories generate the most profit?**

These questions provide a practical view of **revenue performance, customer value, demand patterns, product performance, and profitability**.

---

## 🔄 ETL & Database Pipeline

```text
Raw Superstore Dataset
        │
        ▼
Python / Pandas
Data Cleaning & Preparation
        │
        ▼
MySQL Staging Layer
        │
        ▼
Data Transformation & Validation
        │
        ▼
Normalized 3NF Database
        │
        ├── Customers
        ├── Products
        ├── Orders
        └── Order_Details
        │
        ▼
SQL Business Queries
        │
        ▼
Business Insights & HTML Outputs

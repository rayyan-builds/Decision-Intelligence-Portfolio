# Retail Sales ETL & SQL Analytics

An end-to-end retail data pipeline project demonstrating ETL, relational database design, SQL-based data migration, and business analytics using a modified Superstore retail dataset.

## Overview

This project transforms raw retail transaction data into a structured and analysis-ready relational database.

The pipeline takes data from CSV and Excel sources, performs data cleaning and validation using Python, loads the cleaned data into a staging layer, and migrates it into a normalized SQL database designed in Third Normal Form (3NF).

The resulting database is then queried using SQL to generate business insights around revenue, customers, products, sales trends, and profitability.

## Project Workflow

Raw CSV / Excel Data
        ↓
Data Extraction
        ↓
Data Cleaning & Validation
        ↓
SQL Staging Layer
        ↓
Normalized Relational Database
        ↓
SQL Data Migration
        ↓
Business Analysis & Insights

## ETL Process

### 1. Extract

Data was extracted from two source formats:

- CSV
- Excel

Python and Pandas were used to load the source data into a unified structure.

### 2. Transform

The raw data contained missing values, duplicates, inconsistent formats, and validation issues.

The transformation process included:

- Handling missing numerical and categorical values
- Removing duplicate records
- Standardizing date formats
- Cleaning text fields
- Validating email formats
- Cleaning phone numbers
- Preparing data for relational database loading

### 3. Load

Cleaned data was first loaded into SQL staging tables.

The staging layer acts as an intermediate area between the raw data and the final relational database, making the pipeline easier to validate, debug, and manage.

## Database Design

The original dataset contained customers, products, orders, and location information in a single flat structure.

The data was redesigned into a normalized relational database consisting of:

- Customers
- Orders
- Products
- Locations
- Order_Details

The database follows Third Normal Form (3NF), with primary and foreign keys used to establish relationships and maintain referential integrity.

## SQL & Business Analytics

SQL is a core component of this project.

SQL scripts were used to migrate data from the staging layer into the normalized reporting layer and to perform business-focused analysis.

Key analyses include:

- Revenue analysis
- Customer performance analysis
- Sales trend analysis
- Product performance analysis
- Profitability analysis by product category

The queries demonstrate how a properly structured relational database can support analytical and business decision-making.

## Technologies Used

- Python
- Pandas
- SQL
- MySQL
- Excel
- CSV
- Relational Database Design
- Entity-Relationship Diagrams (ERD)

## Key Challenges

The project involved several practical data engineering challenges:

- Handling missing values without unnecessarily losing records
- Normalizing a flat retail dataset
- Maintaining relationships between database entities
- Preserving referential integrity during migration
- Establishing data validation rules
- Designing SQL queries for meaningful business analysis

## Outcome

The project demonstrates an end-to-end workflow from raw business data to structured data and actionable insights.

It combines data engineering, SQL, database design, and business analytics to create a reliable foundation for retail decision-making.

## Project Structure

```text
Retail-Sales-ETL/
│
├── README.md
├── data/
├── python/
├── sql/
├── database/
└── documentation/

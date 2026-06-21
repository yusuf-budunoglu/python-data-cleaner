# E-Commerce Data Cleaner (ETL Pipeline)

## Overview
This project is a lightweight ETL (Extract, Transform, Load) pipeline built with Python. It automates the process of reading raw, messy e-commerce data from a CSV file, filtering out incomplete records, and exporting the clean data into both CSV and JSON formats for data analysis and system integration.

## Features
* **Data Validation:** Identifies and skips rows with missing critical information (e.g., empty prices or categories).
* **Type Casting:** Converts string-based numerical data into integers for safer mathematical operations.
* **Multi-Format Export:** Outputs the cleaned dataset into `.csv` (for data analysts) and `.json` (for API/AI model integration).

## Tech Stack
* **Language:** Python 3.x
* **Libraries:** `csv`, `json` (Built-in standard libraries)

## How It Works
1. Reads raw data from `products.csv`.
2. Validates each row. If a row is missing a Category or Price, it logs an error and skips the row.
3. If the row is clean, it appends it to a secure list in memory.
4. Finally, it exports the clean data into `clean_products.csv` and `clean_products.json`.

# Fraud-Detection-Anomoly-Analysis
Fraud Detection &amp; Anomoly Analysis dashboard using python, DuckDB and Matplotlib

## Project Overview
This project builds an end-to-end fraud detection and anomaly analysis system using:
- DuckDB+ MotherDuck (Cloud Data Warehouse)
- SQL for data cleaning, feature engineering & risk scoring
- Python for modeling and statistical analysis
- Matplotlib & Plotly for visualization dashboards

### The goal is to:
- Detect fraudulent transactions
- Engineer fraud risk scores
- Perform statistical anomaly detection
- Visualize fraud patterns interactively
- Build a portfolio-ready data analytics project

## Project Structure

Workflow:
Raw CSV Data → Cloud Data Warehouse (MotherDuck) → Data Cleaning & Transformation → Feature Engineering → Fraud Analytics → Python Visualizations

fraud-detection-motherduck/
│
├── python/
│   ├── run_sql.py
│   ├── modeling.py
│   ├── visuals_matplotlib.py
│   └── visuals_plotly_dashboard_full.py
│
├── sql/
│   ├── 00_check_data.sql
│   ├── 01_load_data.sql
│   ├── 02_clean_data.sql
│   ├── 03_feature_engineering.sql
│   ├── 04_analysis.sql
│   ├── 05_advanced_analysis.sql
│   └── 06_risk_scoring.sql
│
├── fraud_analysis_portfolio.png
├── requirements.txt
├── README.md
└── .gitignore


## Problem Statement

Credit card fraud detection is a classic anomaly detection problem where fraudulent transactions represent a very small fraction (-0.16%) of total transactions.

### Key challenges:
 - Highly imbalanced dataset
 - Fraud patterns hidden in complex features
 - Need for statistical anomaly detection
 - Need for interpretable risk scoring

## End-to-End Workflow

1. Data Loading (SQL. + MotherDuck)
 - Connected to MotherDuck cloud warehouse
 - Loaded transaction dataset into DuckDB
 - Verified structure and schema

2. Data Cleaning
 - Checked null values
 - Veriled data types
 - Created structured fraud analysis tables

3. Feature Engineering
Created new features such as
 - Amount categories (Low/Medium/High)
 - Log-transformed transaction amount
 - Risk components:
        a. Amount risk
        b. Z-score anomaly risk
        c. Fraud probability risk

4. Fraud Risck Scoring System (SQL)
      Total Risk Score =
    Amount Risk
  + Z-Score Risk
  + Fraud Pattern Risk

5. Statistical Anomaly Detection
 - Z-Score analysis
 - Identified outliers (|z| > 3)
 - Highlighted extreme transactions
 - Detected unusual spending behavior

6. Advanced Analytics
Performed:
 - Fraud rate by amount category
 - Fraud rate by risk score
 - Log-bucket analysis
 - High-risk transaction segmentation

Example Insight:
 - Low-amount transactions surprisingly showed higher fraud rate than medium.
 - Extreme Z-score transactions strongly correlated with fraud.

## Key Findings
 - Fraud represents only -0.16% of transactions.
 - Low-value transactions can be high fraud-risk.
 - Log transformation improves anomaly detection visibility.
 - High total risk score strongly correlates with fraud.
 - Statistical anomaly detection complements fraud classification.

## Tech Stack
SOL
DuckDB
Mother Duck
Python
Pandas
Matplotlib
Plotly
Git & GitHub


## Why This Project Matters
This project demonstrates:
 - Real-world fraud detection workflow
 - Cloud data warehouse usage
 - SQL-based feature engineering
 - Statistical anomaly detection
 - Risk modeling
 - Data storytelling through visualization
 - End-to-end analytics pipeline






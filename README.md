# Position Control Framework

This project simulates a real-world trading scenario where we validate position-level P&L (Profit and Loss) and assess data quality using SQL, Python, and Dockerized SQL Server. It demonstrates how Business Analysts and Data Analysts can proactively detect data integrity issues in financial datasets.

---

## Business Objective

In trading operations, inaccurate or misaligned position-level P&L reporting can lead to regulatory violations, financial losses, or misinformed trading decisions.  
The **Position Control Framework** is designed to:

- Validate that calculated P&L aligns with the recorded P&L.
- Identify discrepancies caused by data issues (e.g., missing fields, incorrect execution prices).
- Automate reporting for audit and operational transparency.

---

## Technology Stack

- **Python**: Data generation, transformation, and integration with SQL Server (`pandas`, `faker`, `pyodbc`)
- **SQL Server** (Docker): Relational database to simulate trading tables
- **SQL**: Business logic and validation logic
- **Docker**: Containerized database environment for easy setup and teardown

---

## Project Structure

| File | Description |
|------|-------------|
| `generate_data.py` | Generates 1000 synthetic trade records using `faker` |
| `trading_data.csv` | Generated trading dataset |
| `sql.py` | Inserts trading data into SQL Server using `pyodbc` |
| `pnl_validation.csv` | Output of position-level P&L validation checks |
| `missing_data_report.csv` | Data quality report showing null/missing fields |
| `README.md` | This documentation |

---

## Database Schema

Table: `trading_data`

| Column          | Type         |
|-----------------|--------------|
| trade_id        | VARCHAR(10)  |
| symbol          | VARCHAR(10)  |
| quantity        | INT          |
| execution_price | FLOAT        |
| market_price    | FLOAT        |
| side            | VARCHAR(10)  |
| execution_time  | DATETIME2    |
| pnl             | FLOAT        |

---


## Key Outcomes

- **Validation Accuracy**: 98.7% of records passed the position-level P&L check.
- **Completeness Check**: No missing/null fields detected across 1000 trade entries.
- **Generated Reports**:
  - `pnl_validation.csv`: P&L match vs. mismatch results.
  - `missing_data_report.csv`: Summary of field-level completeness checks.

---

## Potential Extensions

- **Anomaly Detection**: Integrate machine learning models to flag abnormal P&L patterns.
- **BI Dashboard**: Build Power BI or Looker Studio dashboards for interactive reporting.
- **Scheduled Audits**: Automate validation logic on a recurring basis using cron jobs or Airflow.
- **Alert Mechanism**: Notify analysts if mismatch ratios exceed defined thresholds.

---

## Summary

The **Position Control Framework** demonstrates how Business Analysts and Data Analysts can:

- Simulate and audit trade data under realistic financial assumptions.
- Validate integrity using SQL-based logic within a Dockerized environment.
- Generate transparent, traceable outputs suitable for compliance and internal controls.
- Deliver scalable, testable, and business-aligned data quality solutions.
## Validation Coverage

The framework applies two complementary data quality checks:

- **P&L Validation Logic**: Ensures alignment between expected and recorded P&L by applying a tolerance-based comparison formula.
- **Missing Field Audit**: Scans for null/missing values in critical fields (e.g., `trade_id`, `execution_price`, `pnl`) to ensure schema completeness.

Both validations are executed across 1000 rows of synthetic trade data, providing a solid baseline for real-world extension.

---


## Validation Logic

** P&L Validation Formula**

```sql
CASE 
    WHEN ABS((market_price - execution_price) * quantity - pnl) < 0.01 THEN 'OK'
    ELSE 'Mismatch'
END AS pnl_validation
---

## Author

**Ahmet Güçlü**  
*Senior Business Analyst*  
[LinkedIn Profile](https://www.linkedin.com/in/ahmet-guclu-7907992a5/)  
Experience in Capital Markets, Trade Lifecycle, and Data Quality Governance.

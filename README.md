# Audit Analytics Dashboard — SEC Financial Data (2025 Q4)

<img width="1704" height="793" alt="sec-audit-project" src="https://github.com/user-attachments/assets/db5aa0f6-093a-4de5-b5dd-31c789a25948" />

An internal audit analytics tool built in Python that ingests public SEC EDGAR 
financial filings, runs statistical anomaly detection tests, and visualizes 
findings in an interactive dashboard.

Built largely in an effort to gain exposure to industry habits and learn 
relevant skills and techniques.

---

## What It Does

### 1. Benford's Law Analysis
Benford's Law states that across natural financial data, there is a distribution
that holds true. Any large deviation is cause for investigation as it suggests
manipulation, rounding bias or data quality issues.

**Finding:** Digit 1 was under-represented by 4.84% relative to Benford's Law at 
30.1%, the largest deviation in the dataset. Digits 4 and 6 were moderately 
over-represented. These findings could warrant further investigation at the 
company-specific level.

<img width="1704" height="793" alt="sec-audit-project" src="https://github.com/user-attachments/assets/6e521c03-208a-48ab-aefa-6eca34bb340f" />

### 2. Outlier Detection (Z-Score by Industry)
Grouping by industry, this test observes whether any given company reports
abnormal revenues compared to their peers. This allows for accurate comparison.

**Finding:** Intuit Inc. flagged as a statistical outlier within Prepackaged 
Software with Z-scores of 3.63 and 3.10 across two periods. 
Consistent flagging across periods suggests they are genuinely just a larger
company than any competitor and have some form of a moat / competetive advantage.

<img width="1679" height="221" alt="Screenshot 2026-05-16 at 22 53 29" src="https://github.com/user-attachments/assets/0c88cac0-4d90-4472-a610-a1f9beecd8f1" />

### 3. Duplicate Filing Detection
Searches for companies reporting identical revenue figures across multiple 
submissions, which can suggest retroactively amending filings, copy-paste 
errors, or data quality issues.

**Finding:** 105 duplicate revenue figures detected, most of those are
amended filings (10-K/A) and thus should be ignored. 

<img width="1671" height="885" alt="Screenshot 2026-05-16 at 22 53 49" src="https://github.com/user-attachments/assets/9c2c91f5-64ad-4bf4-b03b-b3cc80c3861b" />

---

## Tech Stack

| Tool | Purpose |
|---|---|
| Python 3.11 | Core language |
| Pandas | Data ingestion, cleaning, transformation |
| SciPy | Z-score statistical analysis |
| Plotly / Dash | Interactive dashboard and visualizations |
| SEC EDGAR DERA | Public financial data source |

---

## Data Source

SEC EDGAR Financial Statement Data Sets — publicly available quarterly 
structured financial data from all SEC-registered companies.

https://www.sec.gov/dera/data/financial-statements

Dataset used: 2025 Q4 (num.txt, sub.txt)
(files were too large to upload)

---

## Project Structure

sec-audit-dashboard/
│
├── sec_analysis.ipynb       # Data cleaning, Benford's Law, outlier detection
├── dashboard.py             # Plotly Dash interactive dashboard
├── revenues_final.csv       # Processed output from notebook
├── environment.yml          # Conda environment file
└── README.md

---

## How This Would Extend in a Real Audit Context

- **ML anomaly detection:** Replace Z-score with Isolation Forest or 
  Autoencoder models for unsupervised anomaly detection across more variables
- **Time series analysis:** Track revenue trajectories per company across 
  multiple quarters to flag sudden unexplained jumps
- **Cross-statement testing:** Join revenue data with cash flow statements 
  to flag companies where revenue growth doesn't match cash generation
- **Automated alerts:** Schedule pipeline to run on each new EDGAR quarterly 
  release and flag net-new anomalies automatically

---

## Author

Joshua Hey

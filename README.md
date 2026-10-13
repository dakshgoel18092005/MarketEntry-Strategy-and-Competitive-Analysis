# ⚡ BESS India Market Entry Strategy & Competitive Analysis

> **A quantitative strategy consulting and data analytics portfolio project evaluating the Battery Energy Storage Systems (BESS) market entry into India.**

[![MySQL](https://img.shields.io/badge/MySQL-8.0+-blue.svg?logo=mysql&logoColor=white)](https://dev.mysql.com/)
[![Python](https://img.shields.io/badge/Python-3.14+-3776AB.svg?logo=python&logoColor=white)](https://www.python.org/)
[![Analytics](https://img.shields.io/badge/Analytics-CTEs%20%26%20Window%20Functions-success.svg)]()
[![Financial-Model](https://img.shields.io/badge/Financial%20Model-Sensitivity%20Analysis-orange.svg)]()

---

## 📌 Executive Summary

India is expanding towards a **500 GW non-fossil energy target by 2030**, causing grid instability and widening the gap between peak and off-peak electricity prices. While incumbent conglomerates compete over low-margin central utility auctions, this project identifies and models a high-margin **$90M+ market opportunity in the Commercial & Industrial (C&I) sector**.

This repository delivers an end-to-end analytical framework covering:
1. **A MySQL Weighted Scoring Model** using CTEs and window functions to prioritize 5 state power corridors.
2. **A 3-Year Financial Revenue & Sensitivity Model** evaluating CAC optimization, account retention, and compounding growth.
3. **A 4-Vector Competitive Benchmarking Matrix** identifying two unserved market gaps exploited via an **Energy Storage-as-a-Service (ESaaS)** model.
4. **An Interactive Web Dashboard** featuring real-time weighting simulation and Chart.js visualizations.

---

## 🗂️ Project Repository Structure

```text
dazzling-rutherford/
├── README.md                              # Main portfolio documentation & presentation guide
├── interview_prep_cheatsheet.md           # 5-minute interview review cheat sheet & defense Q&A
├── sql/
│   ├── 01_schema.sql                      # MySQL DDL table definition with indexing & comments
│   ├── 02_seed_data.sql                   # Benchmark power sector metrics for 5 Indian states
│   ├── 03_weighted_scoring_model.sql      # Production CTE & Window function analytical query
│   └── run_sql_demo.py                    # Standalone Python runner (runs query in SQLite memory)
├── financial_model/
│   ├── financial_model.py                 # 3-Year projection & sensitivity matrix generator
│   ├── generate_charts.py                 # Matplotlib chart rendering script
│   ├── 3_year_financial_projections.csv   # Exported Base & Aggressive scenario numbers
│   ├── cac_retention_sensitivity.csv      # Exported 7x7 CAC vs Retention sensitivity grid
│   └── charts/
│       ├── revenue_trajectory.png         # 3-Year revenue scaling chart
│       └── sensitivity_heatmap.png        # Year 3 sensitivity heatmap
├── competitive_analysis/
│   ├── competitor_matrix.csv              # 4-vector comparison dataset (Pricing, Reach, SLA, Value)
│   └── strategy_and_gaps.md               # In-depth strategic whitepaper on the 2 market gaps
└── dashboard/
    └── index.html                         # Interactive Strategy & Analytics Executive Portal
```

---

## 🚀 Quick Start Guide

### 1. Run the SQL Model Locally
You can run the SQL query immediately in your terminal using the Python runner (no live MySQL installation required):
```bash
python sql/run_sql_demo.py
```
*Output:*
```text
=====================================================================================
  INDIA BESS MARKET ENTRY - WEIGHTED SCORING MODEL RESULTS
=====================================================================================
 Rank       State Grid Region  Demand (40%)  Profit (40%)  Comp (20%)  Composite Score  Spread vs Avg             Strategic Phase
    1     Gujarat     Western          92.5          88.0        75.0             77.2            7.6          Wave 1: Anchor Hub
    2 Maharashtra     Western          85.0          82.5        60.0             75.0            5.4 Wave 2: Secondary Expansion
    3  Tamil Nadu    Southern          88.0          65.0        68.0             67.6           -2.0 Wave 2: Secondary Expansion
    4   Rajasthan    Northern          95.0          60.0        85.0             65.0           -4.6       Wave 3: Opportunistic
    5   Karnataka    Southern          78.0          70.0        80.0             63.2           -6.4       Wave 3: Opportunistic
=====================================================================================
```

### 2. Run the 3-Year Financial Model & Generate Charts
```bash
python financial_model/financial_model.py
python financial_model/generate_charts.py
```

### 3. Open the Interactive Strategy Dashboard
Open `dashboard/index.html` directly in any web browser (Chrome, Edge, Safari):
```powershell
Start-Process "dashboard/index.html"
```
Or serve via Python:
```bash
python -m http.server 8000
# Navigate to: http://localhost:8000/dashboard/
```

---

## 📊 Key Highlights for Interview Presentation

### Part 1: The MySQL Scoring Model
* **Formula:**
  $$\text{Composite Score} = (\text{Demand} \times 0.40) + (\text{Profitability} \times 0.40) + ((100 - \text{Competition}) \times 0.20)$$
* **Technical Highlights:**
  * Inverted competition scale ensures all inputs and outputs remain bounded in `[0, 100]`.
  * Multi-layer CTE modularity separates normalization from analytical ranking.
  * Window function `RANK() OVER (ORDER BY composite_market_score DESC)` ensures tie transparency.
  * Window aggregation `AVG() OVER ()` establishes a baseline cohort benchmark without costly self-joins.

### Part 2: The 3-Year Financial Model
* **Spend:** $\$3.1\text{M}$ total marketing spend ($\$600\text{k} \rightarrow \$1.0\text{M} \rightarrow \$1.5\text{M}$).
* **Base Case:** CAC reduces from $\$60\text{k} \rightarrow \$45\text{k}$; Retention improves from $70\% \rightarrow 80\%$.
  * **3-Year Revenue:** **$\$62.70\text{ M}$** ($55$ active accounts).
* **Aggressive Scenario:** CAC optimizes to $\$30\text{k}$; Retention reaches $92\%$.
  * **3-Year Revenue:** **$\$90.05\text{ M}$** ($84$ active accounts).
* **The GTM Delta:** **+$27.35M (+43.6%)** incremental revenue on the same marketing expenditure.

### Part 3: Strategic Gaps & Entry Vector
* **Gap 1 (The Capex Hurdle):** Mid-market industrial plants cannot allocate $\$600\text{k}+$ for non-core batteries. We enter via **Energy Storage-as-a-Service (ESaaS)** with zero upfront capital, sharing Time-of-Day (ToD) tariff savings (spread up to ₹8/kWh).
* **Gap 2 (The Service Vacuum):** Foreign OEMs take 4 days to dispatch field support, while local contractors lack battery telemetry. We operate **regional hubs in Ahmedabad & Pune** offering **<12-hour dispatch** with a contractual **99.5% uptime SLA**.

---

## 🛠️ Tech Stack & Methodologies
* **Database & Query Engineering:** MySQL 8.0, CTEs, Window Functions (`RANK`, `AVG OVER`), Dynamic Indexing.
* **Financial Modeling & Python:** Python 3.14, Pandas, NumPy, Matplotlib.
* **Front-end Data Visualization:** HTML5, Tailwind CSS, Chart.js.
* **Strategic Consulting Frameworks:** Porter’s Competitive Benchmarking, Geospatial Attractiveness Matrix, Customer Unit Economics (CAC/LTV/AOV).

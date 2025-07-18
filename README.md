# ✈️ Flight Delay Analysis: Identifying Root Causes from 3M+ US Flights

This project explores over **3 million US domestic flight records** to uncover the key drivers behind delays and cancellations. Using **SQL for data extraction** and **Python (with Plotly + Streamlit)** for interactive dashboards, this analysis delivers actionable insights across years, airports, airlines, routes, and departure times.

## 🚀 Dashboard
Access the live dashboard here:  📎 **[https://flight-delays-analysis-sql-dashboard.streamlit.app](https://flight-delays-analysis-sql-dashboard.streamlit.app)**

## 📌 Objectives

- Identify trends in delays and cancellations over time
- Break down delay causes (Carrier, Weather, NAS, Security, etc.)
- Analyze performance by airport and airline
- Spot high-risk routes and problematic time windows

## ❓ Key Questions Explored

- Which years experienced the most delays and cancellations?
- What are the top reasons for flight delays?
- Which airports and airlines are the most delay-prone?
- Do specific time slots or routes suffer higher delays?

## 🔍 Key Insights

| Section                          | Insight                                                                                                                                   |
|----------------------------------|-------------------------------------------------------------------------------------------------------------------------------------------|
| **1. Delay Trends Over Time**    | **2023** had the highest delay percentage (**39.8%**) and longest average delays (~34 mins), despite having fewer flights than 2019.      |
| **2. Delay Causes**              | **Late Aircraft** and **Carrier-related issues** were the top contributors—both controllable with better airline operations.              |
| **3. Bottlenecks**               | **Cold Bay (AK)** had a 71% delay rate. **JetBlue** and **Frontier** ranked worst for average delays, while **Delta** and **Hawaiian** led in performance. |
| **4. Risky Routes & Times**      | Routes like **SEA–HOU** and **SJU–CVG** showed **100% delay rates**. Flights between **3–5 AM** and **11 PM–12 AM** had the worst delays. |

## 🧰 Tools & Tech

- **SQLite** – Efficient data querying across 3M+ records
- **Python (Pandas, Plotly)** – Data cleaning and visualization
- **Streamlit** – Building the interactive dashboard
- **GitHub** – Version control and deployment integration


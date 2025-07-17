# Flight Delay Analysis: Identifying Root Causes from 3M+ US Flights

The goal of this project is to identify the root causes of flight delays in the United States by analyzing over **3 million domestic flight records**, and uncover operational patterns across years, airports, airlines, routes, and departure times using SQL and Python visualizations helping stakeholders target the biggest contributors to disruption.

##  Key Questions Explored

- Which years experienced the most delays and cancellations?
- What are the top reasons for flight delays (carrier, weather, NAS, etc.)?
- Which airports and airlines are the most delay-prone?
- Do specific time slots or routes suffer higher delays?

## Key Insights

| Section | Insight |
|---------|---------|
| **1. Delay Trends Over Time** | 2023 had the highest delay percentage (39.8%) and longest average delays (~34 mins), despite fewer total flights than pre-COVID years. |
| **2. Delay Causes** | Most delays were due to **Late Aircraft** and **Carrier-related issues**, indicating that airlines can actively reduce delay rates through better operations. |
| **3. Airport & Airline Bottlenecks** | **Cold Bay (AK)** had a 71% delay rate. Airlines like **JetBlue** and **Frontier** had the worst average delays, while **Delta** and **Hawaiian** performed best. |
| **4. High-Risk Routes & Times** | Several routes had **100% delay rates**, especially SEA–HOU and SJU–CVG. Flights between **3–5 AM and 11 PM–12 AM** showed highest delay percentages. |

## Tools Used

- **Python**: Data analysis & visualizations
- **SQLite**: Querying 3M+ rows with efficient filtering
- **Plotly**: Interactive and static charts

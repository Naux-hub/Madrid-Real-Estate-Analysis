\# 🏠 Madrid Real Estate Market Analysis



\## 📌 Project Overview

End-to-end data pipeline analyzing 21,000+ real estate listings in Madrid.

Built with industry-standard tools to uncover pricing patterns across neighborhoods

and identify key factors that drive property values.



\## 🎯 Business Questions

\- Which neighborhoods command the highest price per m²?

\- How much does a pool, parking, or terrace affect the price?

\- What is the average property size and room count per area?



\## 🛠️ Tech Stack

\- \*\*Python \& Pandas\*\* — data extraction and cleaning

\- \*\*dbt + DuckDB\*\* — data transformation and modeling

\- \*\*Streamlit\*\* — interactive dashboard



\## 📁 Project Architecture

1\. `cleaning.py` — extracts raw data, removes outliers, handles nulls

2\. `madrid\_dbt/models/stg\_madrid\_houses.sql` — staging layer

3\. `madrid\_dbt/models/mart\_price\_by\_neighborhood.sql` — pricing per neighborhood

4\. `madrid\_dbt/models/mart\_price\_drivers.sql` — what drives prices

5\. `dashboard.py` — interactive Streamlit dashboard



\## 🏆 Key Insights

\- \*\*Recoletos\*\* is the most expensive neighborhood at 8,392 €/m²

\- Properties with a \*\*pool\*\* command significantly higher prices

\- \*\*New developments\*\* average considerably more than older properties



\## 🚀 How to Run

```bash

python cleaning.py

cd madrid\_dbt \&\& dbt run \&\& cd ..

streamlit run dashboard.py

```


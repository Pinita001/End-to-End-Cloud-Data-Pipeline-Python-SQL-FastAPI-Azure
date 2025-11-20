# 🟩 Cloud Analytics Platform (ETL + FastAPI + Streamlit) — README.md

## ☁️ Cloud-Based Sales & Inventory Intelligence Platform

A cloud-ready analytics system featuring an ETL pipeline, forecasting API, and interactive dashboard.

### 🔍 What This Project Does

* Cleans & processes **1,000+ sales records**
* Generates KPIs (revenue, top products, stock levels)
* Sends data to **FastAPI microservices**
* Displays insights in a **Streamlit dashboard**
* Designed for **Azure deployment**

### 🛠 Tech Stack

* **Python:** Pandas, NumPy
* **API:** FastAPI
* **Cloud:** Azure App Service
* **Dashboard:** Streamlit
* **Database:** SQL / CSV

### 🧱 Architecture

```
Data Source → ETL Pipeline → FastAPI → Streamlit Dashboard → Users
```

### 📁 Folder Structure

```
/etl
   └── pipeline.py
/api
   ├── main.py
   └── forecast.py
/dashboard
   └── app.py
```
### ☁️ Deployment (Azure)

* Azure App Service (API hosting)
* Azure Storage (data files)
* Streamlit Cloud or Azure Container Apps (dashboard)

### 📌 Future Improvements

* Add Docker containerisation
* Add CI/CD (GitHub Actions)
* Migrate to Azure SQL Database
* Add authentication for the dashboard

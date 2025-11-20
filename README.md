# 📘 End-to-End Cloud Data Pipeline (Python, SQL, FastAPI, AWS)

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.10-blue" />
  <img src="https://img.shields.io/badge/FastAPI-Backend-success" />
  <img src="https://img.shields.io/badge/Streamlit-Dashboard-red" />
  <img src="https://img.shields.io/badge/Azure-Deployment-blueviolet" />
  <img src="https://img.shields.io/badge/Status-In%20Progress-yellow" />
</p>

## 🚀 Overview

This project is an end-to-end, cloud-ready data pipeline designed to simulate a real enterprise analytics workflow. It integrates Python-based ETL processing, SQL transformations, a FastAPI backend, and an interactive Streamlit analytics dashboard.

The system is structured for scalable deployment on **AWS (S3, Lambda, RDS, API Gateway)** and demonstrates cloud-native architecture, data engineering fundamentals, and production-minded API design.

This project demonstrates my ability to build production-minded data pipelines suitable for analytics workflows, cloud deployment, and real-time dashboarding at scale.

---

## ⭐ Features

### ✅ Implemented

* **Python ETL pipeline** for ingestion, cleaning, validation, and transformation of sales & inventory data
* **SQL schema + transformations** for analytics and reporting
* **FastAPI backend** exposing analytical and forecasting endpoints
* **Streamlit dashboard** with product filters, KPIs, and low-stock alerts
* **AWS-ready project structure** using S3, Lambda, and RDS

### 🔧 In Progress

* Automated **AWS deployment pipeline** (GitHub Actions → AWS)
* Scheduled ETL job via **AWS Lambda / EventBridge**
* Authentication for API + dashboard
* Additional forecasting models

---

## 🏗️ Architecture

```
        ┌─────────────────────────┐
        │        Raw Data         │
        └─────────────┬───────────┘
                      ↓
              Python ETL (Pandas)
                      ↓
        ┌─────────────────────────┐
        │     AWS S3 / RDS        │
        └─────────────┬───────────┘
                      ↓
              FastAPI Backend
     (AWS Lambda + API Gateway)
                      ↓
            Streamlit Dashboard
                 (AWS EC2)
                      ↓
               End Users / UI
```

---

## 📂 Tech Stack

**Languages & Tools:**

* Python, SQL
* Pandas, Pydantic
* FastAPI, Uvicorn
* Streamlit

**Cloud (AWS):**

* S3 (storage)
* Lambda (serverless compute)
* API Gateway (REST endpoints)
* RDS (database)
* EC2 (dashboard deployment target)

---

## 🖥️ Screenshots

*(Add your UI + dashboard screenshots here)*

---

## 🛠️ Setup

### 1️⃣ Clone the repository

```bash
git clone <repo-url>
cd cloud-pipeline
```

### 2️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

### 3️⃣ Run the FastAPI backend

```bash
uvicorn main:app --reload
```

### 4️⃣ Run the Streamlit dashboard

```bash
streamlit run dashboard.py
```

---

## 📌 Future Enhancements

* Full CI/CD pipeline with GitHub Actions → AWS
* API authentication + rate limiting
* Caching layer (Redis / CloudFront)
* Expanded dashboard analytics (forecasting, anomaly detection)
* Infrastructure-as-Code (Terraform or AWS CDK)

---

# System Architecture

# Overview

The Digital Payments & Fraud Risk Analytics System follows a modern analytics pipeline that transforms raw transaction data into actionable business insights.

The system consists of five major layers:

1. Data Generation
2. Data Storage
3. Data Processing
4. Business Intelligence
5. Decision Support

---

# Architecture Diagram

```text
                    ┌────────────────────────┐
                    │  Python Data Generator │
                    │ (Synthetic Transactions)│
                    └────────────┬───────────┘
                                 │
                                 ▼
                    ┌────────────────────────┐
                    │   CSV Transaction Data │
                    └────────────┬───────────┘
                                 │
                                 ▼
                    ┌────────────────────────┐
                    │     PostgreSQL DB      │
                    │   Transactions Table   │
                    └────────────┬───────────┘
                                 │
                                 ▼
                    ┌────────────────────────┐
                    │      SQL Analytics     │
                    │ KPI & Business Queries │
                    └────────────┬───────────┘
                                 │
                                 ▼
                    ┌────────────────────────┐
                    │      Power BI          │
                    │ Interactive Dashboards │
                    └────────────┬───────────┘
                                 │
                                 ▼
                    ┌────────────────────────┐
                    │ Business Insights &    │
                    │ Decision Support       │
                    └────────────────────────┘
```

---

# System Components

## 1. Data Generation Layer

Synthetic payment transactions are generated using Python to simulate a realistic digital payment ecosystem.

Generated attributes include:

* Transaction ID
* User ID
* Transaction Time
* Amount
* Payment Method
* Merchant
* City
* Device Type
* Transaction Status
* Failure Reason
* Retry Count
* Latency
* Fraud Flag
* Risk Score

---

## 2. Data Storage Layer

The generated transaction dataset is imported into PostgreSQL.

The database provides:

* Structured storage
* Fast querying
* Data integrity
* Scalability for analytics

---

## 3. Analytics Layer

SQL queries are used to calculate:

* Operational KPIs
* Fraud KPIs
* Merchant KPIs
* Customer KPIs
* Payment Performance Metrics

These queries transform raw transactional data into meaningful business information.

---

## 4. Visualization Layer

Power BI is used to develop interactive dashboards for different business stakeholders.

The dashboards include:

* Executive Dashboard
* Fraud Risk Analytics Dashboard
* Payment Operations Dashboard
* Merchant & Customer Insights Dashboard

Interactive slicers allow users to filter reports by:

* Date
* City
* Payment Method
* Merchant

---

## 5. Business Intelligence Layer

The final analytics layer provides actionable insights that support business decision-making.

Examples include:

* Payment ecosystem monitoring
* Fraud detection and monitoring
* Merchant performance evaluation
* Customer transaction analysis
* Operational performance tracking

---

# Benefits of the Architecture

* Modular and scalable design
* Separation of data generation, storage, analysis, and visualization
* Supports real-world analytics workflows
* Easy to extend with machine learning models or real-time data sources
* Demonstrates an end-to-end fintech analytics pipeline


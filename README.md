# 💳 Digital Payments & Fraud Risk Analytics System

An end-to-end **FinTech Analytics** project that simulates a real-world digital payment ecosystem using synthetic transaction data. The project combines **Python**, **PostgreSQL**, **SQL**, and **Power BI** to monitor payment operations, detect fraudulent activities, evaluate merchant performance, and generate business intelligence through interactive dashboards.

---

## 📌 Project Overview

The Digital Payments & Fraud Risk Analytics System was developed to replicate the analytics workflow used by modern payment companies. It demonstrates how transaction data can be transformed into actionable business insights through data engineering, SQL analytics, and interactive business intelligence dashboards.

The project covers the complete analytics pipeline:

* Synthetic payment transaction generation using Python
* PostgreSQL database design and management
* SQL-based operational and fraud analytics
* KPI development using DAX
* Interactive Power BI dashboards
* Business insights and recommendations

---

## 🎯 Business Problem

Digital payment platforms process millions of transactions every day. Payment failures, fraud attempts, high transaction latency, and merchant performance issues can directly impact customer experience and business revenue.

This project provides an analytics solution to help organizations:

* Monitor payment ecosystem health
* Detect fraudulent transactions
* Analyze payment failures
* Evaluate merchant performance
* Understand customer transaction behavior
* Support data-driven business decisions


## 🛠️ Technology Stack

| Category              | Technology                        |
| --------------------- | --------------------------------- |
| Programming Language  | Python                            |
| Database              | PostgreSQL                        |
| Data Processing       | Pandas, NumPy                     |
| Data Generation       | Python (Synthetic Data Generator) |
| Query Language        | SQL                               |
| Business Intelligence | Power BI                          |
| IDE                   | Visual Studio Code                |
| Version Control       | Git & GitHub                      |

---

## 🏗️ System Architecture

```text
                Synthetic Data Generation
                         │
                         ▼
               Python Data Generator
                         │
                         ▼
                Transaction Dataset (CSV)
                         │
                         ▼
                  PostgreSQL Database
                         │
                         ▼
                  SQL Analytics Layer
                         │
                         ▼
              Power BI Interactive Dashboards
                         │
                         ▼
          Business Insights & Decision Support
```

---

## ⚙️ Analytics Workflow

1. Generate realistic synthetic transaction data using Python.
2. Validate and clean the generated dataset.
3. Load transaction data into PostgreSQL.
4. Perform SQL-based business and fraud analytics.
5. Create DAX measures and KPIs in Power BI.
6. Build interactive dashboards for different business users.
7. Generate business insights and recommendations for decision-making.

## 📂 Project Structure

```text
Digital-Payments-Fraud-Risk-Analytics-System/
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── synthetic/
│
├── power_bi/
│   ├── Fintech_Analytics.pbix
│   └── screenshots/
│       ├── executive_dashboard.png
│       ├── fraud_risk_dashboard.png
│       ├── payment_operations_dashboard.png
│       └── merchant_customer_dashboard.png
│
├── reports/
│   ├── 01_Project_Overview.md
│   ├── 02_Business_Problem.md
│   ├── 03_System_Architecture.md
│   ├── 04_Data_Dictionary.md
│   ├── 05_KPI_Definitions.md
│   ├── 06_Dashboard_Guide.md
│   ├── 07_Key_Insights_and_Recommendations.md
│   └── 08_Final_Project_Report.md
│
├── scripts/
│   ├── generate_data.py
│   ├── insert_data.py
│   ├── check_data.py
│   └── db_connect.py
│
├── sql/
│   ├── schema.sql
│   ├── analytics_queries.sql
│   └── advanced_kpis.sql
│
├── notebooks/
│
├── requirements.txt
├── README.md
└── LICENSE
```

### Folder Description

| Folder             | Purpose                                                                 |
| ------------------ | ----------------------------------------------------------------------- |
| `data/`            | Stores raw, processed, and synthetic datasets                           |
| `power_bi/`        | Power BI project file and dashboard screenshots                         |
| `reports/`         | Project documentation and business reports                              |
| `scripts/`         | Python scripts for data generation, validation, and database operations |
| `sql/`             | Database schema, SQL analytics queries, and KPI queries                 |
| `notebooks/`       | Exploratory data analysis (optional)                                    |
| `README.md`        | Project overview and setup guide                                        |
| `requirements.txt` | Python package dependencies                                             |

```
```

## 📊 Dashboard Preview

The project consists of four interactive Power BI dashboards designed for different business stakeholders.

---

### 1️⃣ Executive Dashboard

**Purpose**

Provides a high-level overview of the digital payment ecosystem, including transaction volume, payment success, operational performance, and payment channel distribution.

**Key KPIs**

* Total Transactions
* Total Payment Volume
* Success Rate
* Failure Rate
* Average Latency

![2 power_bi/screenshot/executive_dashboard.png](<2 power_bi/screenshot/executive_dashboard.png>)


---

### 2️⃣ Fraud Risk Analytics Dashboard

**Purpose**

Monitors fraudulent activities, financial exposure, high-risk transactions, and fraud distribution across cities and payment methods.

**Key KPIs**

* Fraud Transactions
* Fraud Rate
* Fraud Exposure Amount
* High-Risk Transactions

![fraud Dashbored](<2 power_bi/screenshot/fraud_dashboard.png>)

---

### 3️⃣ Payment Operations Dashboard

**Purpose**

Tracks payment reliability, operational efficiency, transaction latency, retry behavior, and failure analysis.

**Key KPIs**

* Average Latency
* Failure Rate
* Failed Transactions
* Retry Rate

![Payment Operations Dashboard](<2 power_bi/screenshot/payment_operations_dashboard.png>)

---

### 4️⃣ Merchant & Customer Insights Dashboard

**Purpose**

Analyzes merchant performance, customer activity, payment method usage, and revenue contribution.

**Key KPIs**

* Total Merchants
* Total Customers
* Average Transaction Value
* Total Revenue

![Merchant_customer](<2 power_bi/screenshot/merchant_customer.png>)

## 🚀 Installation & Setup

Follow the steps below to run the project locally.

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/Digital-Payments-Fraud-Risk-Analytics-System.git
cd Digital-Payments-Fraud-Risk-Analytics-System
```

---

### 2. Create a Virtual Environment (Optional)

```bash
python -m venv venv
```

Activate the environment:

**Windows**

```bash
venv\Scripts\activate
```

**Linux / macOS**

```bash
source venv/bin/activate
```

---

### 3. Install Dependencies

```bash
pip install -r requirements.txt
```

---

### 4. Configure PostgreSQL

Create a PostgreSQL database named:

```text
fintech_analytics
```

Update your database credentials in:

```text
scripts/db_connect.py
```

and

```text
scripts/insert_data.py
```

---

### 5. Generate Synthetic Data

```bash
python scripts/generate_data.py
```

---

### 6. Validate the Dataset

```bash
python scripts/check_data.py
```

---

### 7. Load Data into PostgreSQL

```bash
python scripts/insert_data.py
```

---

### 8. Execute SQL Scripts

Run the following SQL files using PostgreSQL or pgAdmin:

* `schema.sql`
* `analytics_queries.sql`
* `advanced_kpis.sql`

---

### 9. Open Power BI Dashboard

Open:

```text
power_bi/Fintech_Analytics.pbix
```

Refresh the PostgreSQL connection if required.

---

## 📦 Project Requirements

* Python 3.10+
* PostgreSQL 14+
* Power BI Desktop
* Visual Studio Code (recommended)

---

## ✅ Project Workflow

1. Generate synthetic transaction data.
2. Store data in PostgreSQL.
3. Execute SQL analytics queries.
4. Build Power BI dashboards.
5. Analyze KPIs and business insights.
6. Support data-driven decision-making.

## 📈 Key Project Highlights

* End-to-end FinTech analytics solution
* Generated and analyzed **100,000+ synthetic payment transactions**
* Designed a normalized PostgreSQL database
* Developed **20+ SQL analytics queries** for business intelligence
* Built **4 interactive Power BI dashboards**
* Created business-focused KPIs and DAX measures
* Simulated fraud detection using a rule-based risk scoring model
* Documented the complete analytics workflow with professional reports

---

## 💼 Skills Demonstrated

### Data Analytics

* SQL
* Power BI
* Data Visualization
* KPI Development
* Business Intelligence

### Data Engineering

* Data Generation
* PostgreSQL
* Data Modeling
* ETL Concepts

### Python

* Pandas
* NumPy
* Synthetic Data Generation

### Business Domain

* Digital Payments
* Payment Operations
* Fraud Risk Analytics
* Merchant Performance Analysis
* Customer Analytics

---

## 🔮 Future Enhancements

* Real-time payment transaction streaming
* Machine Learning-based fraud detection
* Customer segmentation using clustering
* Predictive payment failure analysis
* Automated fraud alert system
* Cloud deployment (AWS/Azure)
* REST API integration
* Real-time dashboard refresh

---

## 👨‍💻 Author

**Lakhanpal**

B.Tech Computer Science Engineering

Aspiring **FinTech Data Analyst | Data Analyst | Data Engineer**

**Skills:** Python, SQL, PostgreSQL, Power BI, Pandas, NumPy

---

## 📜 License

This project is licensed under the MIT License.

---

## ⭐ Support

If you found this project useful, consider giving it a ⭐ on GitHub.

Feedback, suggestions, and contributions are always welcome.





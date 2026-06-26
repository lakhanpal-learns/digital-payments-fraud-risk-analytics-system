# Data Dictionary

## Overview

This document describes the structure of the transaction dataset used in the **Digital Payments & Fraud Risk Analytics System**. It defines each field, its data type, business meaning, and purpose within the analytics workflow.

---

# Transactions Table

| Column Name        | Data Type     | Description                                                              | Business Purpose                               |
| ------------------ | ------------- | ------------------------------------------------------------------------ | ---------------------------------------------- |
| transaction_id     | VARCHAR       | Unique identifier for each transaction                                   | Used for transaction tracking and auditing     |
| user_id            | VARCHAR       | Unique identifier for each customer                                      | Customer behavior and transaction analysis     |
| transaction_time   | TIMESTAMP     | Date and time when the transaction occurred                              | Time-series analysis and peak hour monitoring  |
| amount             | NUMERIC(12,2) | Transaction amount (₹)                                                   | Revenue, payment volume, and spending analysis |
| payment_method     | VARCHAR       | Payment channel used (UPI, Credit Card, Debit Card, Wallet, Net Banking) | Payment channel performance analysis           |
| merchant_name      | VARCHAR       | Merchant receiving the payment                                           | Merchant performance and revenue analysis      |
| city               | VARCHAR       | City where the transaction originated                                    | Geographic transaction and fraud analysis      |
| device_type        | VARCHAR       | Device used to initiate the transaction                                  | Device usage analysis                          |
| transaction_status | VARCHAR       | Status of the transaction (Success / Failed)                             | Payment reliability monitoring                 |
| failure_reason     | VARCHAR       | Reason for transaction failure                                           | Root cause analysis of failed payments         |
| latency_ms         | INTEGER       | Transaction processing time in milliseconds                              | System performance monitoring                  |
| retry_count        | INTEGER       | Number of retry attempts before completion                               | Payment friction and retry behavior analysis   |
| fraud_flag         | INTEGER       | Indicates whether a transaction is fraudulent (1) or legitimate (0)      | Fraud monitoring and risk reporting            |
| risk_score         | INTEGER       | Simulated fraud risk score (0–100)                                       | Risk segmentation and fraud investigation      |

---

# Dataset Summary

| Attribute     | Value                           |
| ------------- | ------------------------------- |
| Dataset Type  | Synthetic                       |
| Domain        | FinTech / Digital Payments      |
| Total Records | 100,000                         |
| Total Columns | 14                              |
| Database      | PostgreSQL                      |
| Source        | Python Synthetic Data Generator |

---

# Business Classification

### Transaction Information

* transaction_id
* transaction_time
* amount
* transaction_status

---

### Customer Information

* user_id
* city
* device_type

---

### Payment Information

* payment_method
* merchant_name
* retry_count
* latency_ms

---

### Risk Information

* fraud_flag
* risk_score
* failure_reason

---

# Data Quality

The dataset was generated with the following characteristics:

* Unique transaction identifiers
* No duplicate transaction records
* No missing values in mandatory fields
* Realistic payment method distribution
* Simulated fraud scenarios using risk-based logic
* Operational metrics including retries and latency
* Balanced distribution suitable for business analytics and dashboarding

---

# Usage

This dataset supports multiple analytical use cases, including:

* Payment Operations Monitoring
* Fraud Risk Analytics
* Merchant Performance Analysis
* Customer Transaction Analysis
* Executive Business Reporting
* KPI Development
* Power BI Dashboarding
* SQL-Based Business Intelligence

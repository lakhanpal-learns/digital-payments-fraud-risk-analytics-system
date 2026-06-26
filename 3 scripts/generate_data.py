import pandas as pd
import numpy as np
import random
from faker import Faker
from datetime import datetime, timedelta

fake = Faker()

# -----------------------------
# CONFIG
# -----------------------------

NUM_TRANSACTIONS = 100000

payment_methods = ["UPI", "Credit Card", "Debit Card", "Wallet", "Net Banking"]

device_types = ["Android", "iOS", "Web"]

cities = [
    "Delhi", "Mumbai", "Bangalore",
    "Chandigarh", "Pune", "Hyderabad",
    "Kolkata", "Chennai"
]

merchants = [
    "Amazon", "Flipkart", "Swiggy",
    "Zomato", "Myntra", "Uber",
    "Paytm", "PhonePe"
]

failure_reasons = [
    "Insufficient Funds",
    "Bank Server Timeout",
    "Network Error",
    "Payment Gateway Error",
    "Suspected Fraud"
]

# -----------------------------
# GENERATE DATA
# -----------------------------

transactions = []

start_date = datetime.now() - timedelta(days=90)

for i in range(NUM_TRANSACTIONS):

    transaction_id = f"TXN{i+1:06d}"

    user_id = f"USER{random.randint(1000, 9999)}"

    transaction_time = start_date + timedelta(
        seconds=random.randint(0, 90 * 24 * 60 * 60)
    )

    # amount = round(np.random.exponential(scale=2500), 2)
    amount = round(np.random.exponential(scale=4000), 2)

    # payment_method = random.choice(payment_methods)
    # improvement 
    payment_method = np.random.choice(
    payment_methods,
    p=[0.60, 0.15, 0.10, 0.10, 0.05]
    )

    merchant_name = random.choice(merchants)

    # city = random.choice(cities)
    city = np.random.choice(
    cities,
    p=[0.22, 0.20, 0.18, 0.10, 0.08, 0.08, 0.07, 0.07]
    )

    device_type = random.choice(device_types)

    hour = transaction_time.hour

    # -----------------------------
    # LATENCY LOGIC
    # Peak hours => more latency
    # -----------------------------

    if 18 <= hour <= 23:
        latency_ms = random.randint(300, 1500)
    else:
        latency_ms = random.randint(100, 700)

    # -----------------------------
    # SUCCESS / FAILURE LOGIC
    # -----------------------------

    success_probability = 0.95

    if latency_ms > 1200:
        success_probability -= 0.10

    transaction_status = np.random.choice(
        ["Success", "Failed"],
        p=[success_probability, 1 - success_probability]
    )

    # -----------------------------
    # FAILURE LOGIC
    # -----------------------------

    if transaction_status == "Failed":
        failure_reason = random.choice(failure_reasons)
        retry_count = random.randint(1, 3)
    else:
        failure_reason = None
        retry_count = 0

    # -----------------------------
    # FRAUD LOGIC
    # -----------------------------

    
        # -----------------------------
# FRAUD LOGIC
# -----------------------------

        fraud_flag = 0
        risk_score = random.randint(10, 30)

        # High amount transactions
        if amount > 15000:
            risk_score += 25

        # Very high amount
        if amount > 30000:
            risk_score += 20

        # Night transactions
        if 0 <= hour <= 4:
            risk_score += 15

        # Multiple retries
        if retry_count >= 2:
            risk_score += 20

        # High latency suspicious
        if latency_ms > 1200:
            risk_score += 10

        # Failed + high amount
        if transaction_status == "Failed" and amount > 10000:
            risk_score += 15

        # Random anomaly simulation
        if random.random() < 0.01:
            risk_score += 25

        # Final fraud classification
        if risk_score >= 50:
            fraud_flag = 1


    transactions.append([
        transaction_id,
        user_id,
        transaction_time,
        amount,
        payment_method,
        merchant_name,
        city,
        device_type,
        transaction_status,
        failure_reason,
        latency_ms,
        retry_count,
        fraud_flag,
        risk_score
    ])

# -----------------------------
# CREATE DATAFRAME
# -----------------------------

columns = [
    "transaction_id",
    "user_id",
    "transaction_time",
    "amount",
    "payment_method",
    "merchant_name",
    "city",
    "device_type",
    "transaction_status",
    "failure_reason",
    "latency_ms",
    "retry_count",
    "fraud_flag",
    "risk_score"
]

df = pd.DataFrame(transactions, columns=columns)

# -----------------------------
# SAVE CSV
# -----------------------------

df.to_csv("data/raw/transactions_update.csv", index=False)

print("Dataset generated successfully!")
print(df.head())
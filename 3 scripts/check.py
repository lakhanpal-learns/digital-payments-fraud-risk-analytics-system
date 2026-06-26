import pandas as pd

# Load dataset
df = pd.read_csv("data/raw/transactions_update.csv")

print("\n==============================")
print("DATASET OVERVIEW")
print("==============================")

print("\nShape of dataset:")
print(df.shape)

print("\nColumns:")
print(df.columns)

print("\nFirst 5 rows:")
print(df.head())

# -----------------------------------
# SUCCESS VS FAILURE
# -----------------------------------

print("\n==============================")
print("TRANSACTION STATUS DISTRIBUTION")
print("==============================")

status_distribution = (
    df["transaction_status"]
    .value_counts(normalize=True) * 100
)

print(status_distribution)

# -----------------------------------
# FRAUD DISTRIBUTION
# -----------------------------------

print("\n==============================")
print("FRAUD DISTRIBUTION")
print("==============================")

fraud_distribution = (
    df["fraud_flag"]
    .value_counts(normalize=True) * 100
)

print(fraud_distribution)

# -----------------------------------
# RETRY ANALYSIS
# -----------------------------------

print("\n==============================")
print("RETRY COUNT DISTRIBUTION")
print("==============================")

print(df["retry_count"].value_counts())

# -----------------------------------
# LATENCY ANALYSIS
# -----------------------------------

print("\n==============================")
print("LATENCY ANALYSIS")
print("==============================")

print(df["latency_ms"].describe())

# -----------------------------------
# AMOUNT ANALYSIS
# -----------------------------------

print("\n==============================")
print("AMOUNT ANALYSIS")
print("==============================")

print(df["amount"].describe())

# -----------------------------------
# MISSING VALUES
# -----------------------------------

print("\n==============================")
print("MISSING VALUES")
print("==============================")

print(df.isnull().sum())

# -----------------------------------
# FRAUD SAMPLE
# -----------------------------------

print("\n==============================")
print("FRAUD SAMPLE TRANSACTIONS")
print("==============================")

fraud_cases = df[df["fraud_flag"] == 1]

print(fraud_cases.head())

# -----------------------------------
# PAYMENT METHOD ANALYSIS
# -----------------------------------

print("\n==============================")
print("PAYMENT METHOD DISTRIBUTION")
print("==============================")

print(df["payment_method"].value_counts())

# -----------------------------------
# CITY DISTRIBUTION
# -----------------------------------

print("\n==============================")
print("CITY DISTRIBUTION")
print("==============================")

print(df["city"].value_counts())

print("\n==============================")
print("DATA QUALITY CHECK COMPLETED")
print("==============================")
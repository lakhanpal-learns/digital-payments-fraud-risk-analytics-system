SELECT
    COUNT(*) AS total_transactions,
    ROUND(SUM(amount), 2) AS total_payment_volume,
    ROUND(AVG(amount), 2) AS avg_transaction_value
FROM transactions;

-- Why This Matters

-- Shows:
-- transaction scale
-- processed volume
-- customer spending behavior

-- Very common fintech KPI.
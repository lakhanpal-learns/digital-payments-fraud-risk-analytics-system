SELECT
    EXTRACT(HOUR FROM transaction_time) AS hour,
    COUNT(*) AS fraud_transactions
FROM transactions
WHERE fraud_flag = 1
GROUP BY hour
ORDER BY fraud_transactions DESC;

-- Identify high-risk transaction windows.

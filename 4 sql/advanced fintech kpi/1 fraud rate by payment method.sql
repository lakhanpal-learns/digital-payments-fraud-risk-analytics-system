SELECT
    payment_method,
    COUNT(*) AS total_transactions,
    SUM(fraud_flag) AS fraud_transactions,
    ROUND(
        SUM(fraud_flag) * 100.0 / COUNT(*),
        2
    ) AS fraud_rate_pct
FROM transactions
GROUP BY payment_method
ORDER BY fraud_rate_pct DESC;

-- Find which payment channel carries more fraud risk.
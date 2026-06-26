SELECT
    DATE(transaction_time) AS transaction_date,
    COUNT(*) AS total_transactions,
    ROUND(SUM(amount),2) AS total_volume
FROM transactions
GROUP BY DATE(transaction_time)
ORDER BY transaction_date;
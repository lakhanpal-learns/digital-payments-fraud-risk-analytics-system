SELECT
    EXTRACT(HOUR FROM transaction_time) AS hour,
    COUNT(*) AS total_transactions
FROM transactions
GROUP BY hour
ORDER BY total_transactions DESC;


-- Business Meaning

-- Important for:

-- traffic forecasting
-- infrastructure scaling
-- operational planning
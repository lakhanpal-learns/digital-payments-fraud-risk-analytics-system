SELECT
    payment_method,
    COUNT(*) AS total_transactions,
    ROUND(AVG(amount), 2) AS avg_amount,
    ROUND(AVG(latency_ms), 2) AS avg_latency
FROM transactions
GROUP BY payment_method
ORDER BY total_transactions DESC;

-- Business Insight Example

-- You may later discover:

-- UPI highest usage
-- cards higher transaction size
-- wallets faster processing

-- This becomes dashboard insight material.
SELECT
    city,
    COUNT(*) AS fraud_transactions
FROM transactions
WHERE fraud_flag = 1
GROUP BY city
ORDER BY fraud_transactions DESC;

-- Business Meaning

-- Helps identify:

-- high-risk geographies
-- targeted monitoring areas

-- Very fintech-relevant.
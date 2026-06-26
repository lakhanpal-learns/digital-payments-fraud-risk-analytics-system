SELECT
    merchant_name,
    COUNT(*) AS fraud_transactions
FROM transactions
WHERE fraud_flag = 1
GROUP BY merchant_name
ORDER BY fraud_transactions DESC;

-- Business Meaning

-- Helps identify:

-- suspicious merchants
-- operational fraud hotspots
SELECT
    fraud_flag,
    COUNT(*) AS total_transactions,
    ROUND(
        COUNT(*) * 100.0 /
        (SELECT COUNT(*) FROM transactions),
        2
    ) AS percentage
FROM transactions
GROUP BY fraud_flag;


-- Business Meaning

-- Measures:

-- suspicious transaction exposure
-- fraud monitoring effectiveness
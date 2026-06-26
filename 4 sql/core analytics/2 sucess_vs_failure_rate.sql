SELECT
    transaction_status,
    COUNT(*) AS total_transactions,
    ROUND(
        COUNT(*) * 100.0 /
        (SELECT COUNT(*) FROM transactions),
        2
    ) AS percentage
FROM transactions
GROUP BY transaction_status;

-- Business Meaning

-- This measures:

-- payment system reliability

-- Low success rate can indicate:

-- bank downtime
-- gateway problems
-- infrastructure strain
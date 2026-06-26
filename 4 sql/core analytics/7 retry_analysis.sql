SELECT
    retry_count,
    COUNT(*) AS transaction_count
FROM transactions
GROUP BY retry_count
ORDER BY retry_count;


-- Business Meaning

-- High retries can indicate:

-- poor payment experience
-- gateway instability
-- customer frustration
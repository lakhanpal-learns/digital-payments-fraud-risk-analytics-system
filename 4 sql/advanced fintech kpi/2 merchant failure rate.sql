SELECT
    merchant_name,
    COUNT(*) AS total_transactions,
    SUM(
        CASE
            WHEN transaction_status = 'Failed'
            THEN 1
            ELSE 0
        END
    ) AS failed_transactions,
    ROUND(
        SUM(
            CASE
                WHEN transaction_status = 'Failed'
                THEN 1
                ELSE 0
            END
        ) * 100.0 / COUNT(*),
        2
    ) AS failure_rate_pct
FROM transactions
GROUP BY merchant_name
ORDER BY failure_rate_pct DESC;


-- why 
-- Detect merchants experiencing payment issues.
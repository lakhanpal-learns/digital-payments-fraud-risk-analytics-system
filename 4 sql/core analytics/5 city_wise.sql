SELECT
    city,
    COUNT(*) AS total_transactions,
    ROUND(SUM(amount), 2) AS total_volume
FROM transactions
GROUP BY city
ORDER BY total_volume DESC;


-- Business Meaning

-- Shows:

-- high activity regions
-- market concentration
-- operational hotspots


SELECT
    payment_method,
    ROUND(AVG(latency_ms),2) AS avg_latency
FROM transactions
GROUP BY payment_method
ORDER BY avg_latency DESC;

-- Measure operational efficiency.
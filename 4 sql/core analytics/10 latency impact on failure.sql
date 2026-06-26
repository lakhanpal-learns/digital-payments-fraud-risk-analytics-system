SELECT
    transaction_status,
    ROUND(AVG(latency_ms), 2) AS avg_latency
FROM transactions
GROUP BY transaction_status;



-- IMPORTANT ANALYST INSIGHT

-- If failed transactions show:

-- much higher latency

-- then:

-- infrastructure delay
-- timeout risk
-- payment degradation

-- may be occurring.

-- This is strong fintech operational analysis.
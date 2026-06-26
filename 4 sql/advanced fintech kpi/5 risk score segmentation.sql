SELECT
    CASE
        WHEN risk_score < 30 THEN 'Low Risk'
        WHEN risk_score < 60 THEN 'Medium Risk'
        ELSE 'High Risk'
    END AS risk_category,
    COUNT(*) AS total_transactions
FROM transactions
GROUP BY risk_category;
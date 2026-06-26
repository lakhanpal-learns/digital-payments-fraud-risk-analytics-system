SELECT
    transaction_id,
    amount,
    payment_method,
    city,
    risk_score
FROM transactions
WHERE risk_score >= 70
ORDER BY risk_score DESC;

-- Show transactions requiring immediate review.
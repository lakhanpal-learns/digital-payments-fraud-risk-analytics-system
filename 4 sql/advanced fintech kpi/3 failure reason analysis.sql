SELECT
    failure_reason,
    COUNT(*) AS total_failures
FROM transactions
WHERE transaction_status = 'Failed'
GROUP BY failure_reason
ORDER BY total_failures DESC;

-- Understand the biggest causes of payment failures.
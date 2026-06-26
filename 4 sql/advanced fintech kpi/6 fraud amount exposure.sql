SELECT
    ROUND(SUM(amount),2) AS fraud_amount_volume
FROM transactions
WHERE fraud_flag = 1;

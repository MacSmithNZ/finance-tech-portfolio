-- Total spent per account
SELECT account_id, SUM(amount) AS total_spent
FROM transactions
GROUP BY account_id
ORDER BY total_spent DESC;

-- Transactions above 300
SELECT *
FROM transactions
WHERE amount > 300;
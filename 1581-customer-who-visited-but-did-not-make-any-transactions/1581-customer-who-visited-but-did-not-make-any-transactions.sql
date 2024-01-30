# Write your MySQL query statement below
SELECT v.customer_id, COUNT(*) as count_no_trans
FROM Visits v
LEFT JOIN Transactions t
ON v.visit_id = t.visit_id
where v.visit_id not in (select visit_id from Transactions )
GROUP BY v.customer_id;
# Write your MySQL query statement below
SELECT name, bonus FROM Employee as E
LEFT JOIN Bonus as B
ON E.empID = B.empId
WHERE bonus < 1000 or bonus IS NULL;
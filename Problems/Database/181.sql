# LC/DB 181. Employees Earning More Than Their Managers

# e1 == manager, e2 == employee
SELECT e2.name as Employee 
FROM employee e1 
INNER JOIN employee e2 ON e1.id = e2.managerID
WHERE e1.salary < e2.salary

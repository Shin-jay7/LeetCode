SELECT
    a.Name AS Employee
FROM
    Employee AS a
WHERE EXISTS
(SELECT 1 FROM Employee AS b
 WHERE a.ManagerId = b.Id
 AND a.Salary > b.Salary)
;


SELECT
    a.Name AS Employee
FROM Employee AS a INNER JOIN Employee AS b
    ON a.ManagerId = b.Id
    AND a.Salary > b.Salary
;


SELECT Name AS Employee
FROM Employee AS a
WHERE Salary > (SELECT Salary FROM Employee AS b WHERE a.ManagerId = b.Id)
;


SELECT
    a.Name AS 'Employee'
FROM
    Employee AS a,
    Employee AS b
WHERE
    a.ManagerId = b.Id
    AND a.Salary > b.Salary
;

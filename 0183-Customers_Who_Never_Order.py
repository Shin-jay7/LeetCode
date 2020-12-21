SELECT
    Name
FROM
    Customers
WHERE
    Customers.Id not in (SELECT CustomerId FROM Orders)
;
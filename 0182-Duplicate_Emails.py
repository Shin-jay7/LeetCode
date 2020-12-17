SELECT
    Email
FROM
    (SELECT Email, COUNT(Email) as num
     FROM Person
     GROUP BY Email) AS statistic
WHERE
    num > 1
;
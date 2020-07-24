SELECT DISTINCT
    l1.Num As ConsecutiveNums
FROM
    Logs l1,
    Logs l2,
    Logs l3
WHERE
    l1.Id = l2.Id - 1
    AND l2.Id = l3.Id - 1
    AND l1.Num = l2.Num
    AND l2.Num = l3.Num


SELECT DISTINCT Num AS ConsecutiveNums
FROM (SELECT Num, CASE
        WHEN @record = Num THEN @count := @count+1
        WHEN @record := Num THEN @count := 1 END AS n
      FROM Logs, (SELECT @count := 0, @record := null) r
      ) a
WHERE a.n >= 3;








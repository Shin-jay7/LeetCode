# Use COUNT as Rank by counting how many S2 table scores beat S1 table score
SELECT S.Score, COUNT(S2.Score) AS 'Rank' FROM Scores S,
(SELECT DISTINCT Score FROM Scores) S2
WHERE S.Score <= S2.Score
GROUP BY S.Id
ORDER BY S.Score DESC;


SELECT
    Score,
    @rank := @rank + (@prev <> (@prev := Score)) 'Rank'
FROM
    Scores,
    (SELECT @rank := 0, @prev := -1) init
ORDER BY Score DESC


SELECT
    Score,
    (SELECT COUNT(DISTINCT Score) FROM Scores WHERE Score >= S.Score) 'Rank'
FROM Scores S
ORDER BY Score DESC


SELECT S.Score, COUNT(DISTINCT T.Score) 'Rank'
FROM Scores S JOIN Scores T ON S.Score <= T.Score
GROUP BY S.Id
ORDER BY S.Score DESC





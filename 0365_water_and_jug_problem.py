from __future__ import annotations
from collections import deque
from fractions import gcd


# Bézout's identity (also called Bézout's lemma) 
class Solution:
    def canMeasureWater(
        self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int
    ) -> bool:
        x, y, z = jug1Capacity, jug2Capacity, targetCapacity
        return z == 0 or x + y >= z and z % gcd(x, y) == 0


class Solution:
    def canMeasureWater(
        self, jug1Capacity: int, jug2Capacity: int, targetCapacity: int
    ) -> bool:
        x, y, z = jug1Capacity, jug2Capacity, targetCapacity
        if x + y < z:
            return False
        visited, queue = set(), deque([(0, 0)])

        while queue:
            i, j = queue.popleft()
            visited.add((i, j))
            if i + j == z:
                return True
            moves = set([
                (x, j), (i, y), (0, j), (i, 0),
                (min(i+j, x), (i+j) - min(i+j, x)),
                ((i+j) - min(i+j, y), min(i+j, y)),
            ])
            queue.extend(moves - visited)

        return False

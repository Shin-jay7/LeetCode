from __future__ import annotations
from typing import List


class Solution:
    def isSelfCrossing(self, distance: List[int]) -> bool:
        length = len(distance)
        if length < 4:
            return False

        # Illustration: https://leetcode.com/problems/self-crossing/discuss/79131/Java-Oms-with-explanation/195274
        for i in range(3, length):
            # Fourth line crosses first line and onward
            if distance[i] >= distance[i-2] and distance[i-1] <= distance[i-3]:
                return True
            # Fifth line meets first line and onward
            if i >= 4:
                if distance[i-1] == distance[i-3] and\
                   distance[i] + distance[i-4] >= distance[i-2]:
                    return True
            # Sixth line crosses first line and onward
            if i >= 5:
                if distance[i-2] - distance[i-4] >= 0 and\
                   distance[i] >= distance[i-2] - distance[i-4] and\
                   distance[i-1] >= distance[i-3] - distance[i-5] and\
                   distance[i-1] <= distance[i-3]:
                    return True

        return False

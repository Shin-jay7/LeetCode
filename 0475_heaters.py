from __future__ import annotations
from typing import List
import bisect


class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        heaters = [float('-inf')] + heaters + [float('inf')]
        ans, i = 0, 0
        for house in houses:
            while house > heaters[i+1]:
                i += 1
            dis = min(house - heaters[i], heaters[i+1] - house)
            ans = max(ans, dis)
        return ans


class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        heaters = [float('-inf')] + heaters + [float('inf')]
        ans, i = 0, 0
        for house in houses:
            i = bisect.bisect_right(heaters, house) - 1
            dis = min(house - heaters[i], heaters[i+1] - house)
            ans = max(ans, dis)
        return ans


class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        heaters.sort()
        return max(min(abs(house - heater)
                       for i in [bisect.bisect_right(heaters, house)]
                       for heater in heaters[i-(i > 0):i+1])
                   for house in houses)

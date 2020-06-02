from __future__ import annotations



"""
If proceed from A, and found A cannot reach B, then for any points C
between A and B; C cannot reach B too. (because if A reached C,
then the fuel left when reached C will always >= 0, which means C to B
results in worse negative than a to B.
"""
class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        tank = gap = start = 0
        n = len(gas)

        for i in range(n):
            tank += gas[i]
            if tank >= cost[i]:
                tank -= cost[i]
            else:
                gap += cost[i] - tank
                start = i+1
                tank = 0

        if start == n or tank < gap: return -1

        return start


test = Solution()
test.canCompleteCircuit([1,2,3,4,5], [3,4,5,1,2]) # 3

test = Solution()
test.canCompleteCircuit([2,3,4], [3,4,3]) # -1

from __future__ import annotations
from collections import defaultdict

class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        pre = defaultdict(list)
        for x, y in prerequisites:
            pre[x].append(y)

        status = [0] * numCourses
        def canTake(i):
            if status[i]:
                return status[i] == 1
            status[i] = -1
            if any(not canTake(j) for j in pre[i]):
                return False
            status[i] = 1
            return True

        return all(canTake(i) for i in range(numCourses))


test = Solution()
test.canFinish(2, [[1,0],[0,1]])

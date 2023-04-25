from __future__ import annotations
from typing import List


class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates


class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        emps = {e.id: e for e in employees}

        def dfs(id: int):
            ans = emps[id].importance
            for subordinate in emps[id].subordinates:
                ans += dfs(subordinate)
            return ans

        return dfs(id)

from __future__ import annotations
from typing import List
from collections import defaultdict

# http://www.graph-magics.com/articles/euler.php
class Solution:
    def dfs(self, airport: str) -> None:
        while self.adj_list[airport]:
            candidate = self.adj_list[airport].pop()
            self.dfs(candidate)
        self.route.append(airport)

    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        self.route = []
        self.adj_list = defaultdict(list)
        for i, j in tickets:
            self.adj_list[i].append(j)
        for key in self.adj_list:
            self.adj_list[key] = sorted(self.adj_list[key], reverse=True)
        self.dfs("JFK")

        return self.route[::-1]

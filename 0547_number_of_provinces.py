from __future__ import annotations
from typing import List


# https://www.slideshare.net/chokudai/union-find-49066733/1
# https://note.nkmk.me/python-union-find/
# https://qiita.com/white1107/items/52fd4149bb1846862e38
class UnionFind:
    def __init__(self, lists):
        self.u = list(range(lists))

    def union(self, a, b):
        root_a, root_b = self.find(a), self.find(b)
        if root_a != root_b:
            self.u[root_a] = root_b

    def find_root(self, num):
        while self.u[num] != num:
            num = self.u[num]
        return num


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        if not isConnected:
            return 0
        cities = len(isConnected)
        uf = UnionFind(cities)
        for row_idx in range(cities):
            for col_idx in range(row_idx, cities):
                if isConnected[row_idx][col_idx] == 1:
                    uf.union(row_idx, col_idx)
        return len(set([uf.find(city) for city in range(cities)]))


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        if not isConnected:
            return 0
        cities = len(isConnected)
        visited = set()

        def dfs(city):
            for place, is_connected in enumerate(isConnected[city]):
                if (is_connected == 1) and (place not in visited):
                    visited.add(place)
                    dfs(place)

        provinces = 0
        for city in range(cities):
            if city not in visited:
                dfs(city)
                provinces += 1
        return provinces


class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        if not isConnected:
            return 0
        cities = len(isConnected)
        visited = set()
        provinces = 0
        for city in range(cities):
            if city not in visited:
                cities = [city]
                while cities:
                    place = cities.pop(0)
                    if place not in visited:
                        visited.add(place)
                        cities += [
                             city for city, is_connected
                             in enumerate(isConnected[place])
                             if is_connected and (city not in visited)
                            ]
                provinces += 1
        return provinces

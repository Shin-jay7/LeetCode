from __future__ import annotations


https://leetcode.com/problems/course-schedule-ii/discuss/59321/Python-easy-to-understand-solution-with-comments./431103

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        sortedOrder = []
        if numCourses <= 0:
            return False
        inDegree = {i: 0 for i in range(numCourses)}
        graph = {i: [] for i in range(numCourses)}

        for dest, src in prerequisites:
            graph[src].append(dest)
            inDegree[dest] += 1

        sources = deque()

        for key in inDegree:
            if inDegree[key] == 0:
                sources.append(key)

        while sources:
            vertex = sources.popleft()
            sortedOrder.append(vertex)
            for dest in graph[vertex]:
                inDegree[dest] -= 1
                if inDegree[dest] == 0:
                    sources.append(dest)

        if len(sortedOrder) != numCourses:
            return []

        return sortedOrder

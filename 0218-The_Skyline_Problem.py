from __future__ import annotations
import heapq


class Solution:
    def getSkyline(self, buildings: List[List[int]]) -> List[List[int]]:
        events = []

        for L, R, H in buildings:
            # append start point of building
            events.append((L, -H, R))
            # append end point of building
            events.append((R, 0, 0))

        events.sort()

        res = [[0, 0]]
        hp = [(0, float("inf"))]

        for pos, negH, R in events:
            # pop out building which is end
            while hp[0][1] <= pos:
                heapq.heappop(hp)
            # if it is a start of building, push it into heap as current building
            if negH != 0:
                heapq.heappush(hp, (negH, R))
            # if change in height with previous key point, append to resul
            if res[-1][1] != -hp[0][0]:
                res.append([pos, -hp[0][0]])

        # print(res[1:])
        return res[1:]

                    
test = Solution()
test.getSkyline([[0,2,3],[2,5,3]]) # [[0,3],[5,0]]

test = Solution()
test.getSkyline([[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]) 
# [[2,10],[3,15],[7,12],[12,0],[15,10],[20,8],[24,0]]

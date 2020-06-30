from __future__ import annotations


class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        def helper(currentPoint, points):
            slopes, duplicates, ans = {}, 0, 0
            x1, y1 = currentPoint

            for x2, y2 in points:
                if x1 == x2 and y1 == y2:
                    duplicates += 1
                else:
                    slope = (x2 - x1) / (y2 - y1) if y2 != y1 else 'inf'
                    count = slopes.get(slope, 0) + 1
                    slopes[slope] = count
                    ans = max(ans, count)

            return ans + 1 + duplicates

        ans = 0
        while points:
            currentPoint = points.pop()
            ans = max(ans, helper(currentPoint, points))

        return ans
        # print(ans)


test = Solution()
test.maxPoints([[1,1],[2,2],[3,3]]) # 3

test = Solution()
test.maxPoints([[1,1],[3,2],[5,3],[4,1],[2,3],[1,4]]) # 4

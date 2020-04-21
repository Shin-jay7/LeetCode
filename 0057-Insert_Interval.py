from __future__ import annotations

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int])\
              -> List[List[int]]:
        ans = []
        intervals.append(newInterval)
        intervals.sort()

        for interval in intervals:
            if not ans or ans[-1][1] < interval[0]:
                ans.append(interval)
            else:
                ans[-1][1] = max(ans[-1][1], interval[1])

        return ans
        # print(ans)


test = Solution()
test.insert([[1,3],[6,9]], [2,5]) # [[1,5],[6,9]]

test = Solution()
test.insert([[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]) # [[1,2],[3,10],[12,16]]

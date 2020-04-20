from __future__ import annotations


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        ans = []
        intervals.sort()

        for interval in intervals:
            if not ans or ans[-1][1] < interval[0]:
                ans.append(interval)
            else:
                ans[-1][1] = max(ans[-1][1], interval[1])

        # print(ans)
        return ans


test = Solution()
test.merge([[1,3],[2,6],[8,10],[15,18]]) # [[1,6],[8,10],[15,18]]

test = Solution()
test.merge([[1,4],[4,5]]) # [[1,5]]

test = Solution()
test.merge([[1,4],[2,3]]) # [[1,4]]

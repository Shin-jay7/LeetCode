from __future__ import annotations


class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 0: return []
        if numRows == 1: return [[1]]

        ans = [[1]]

        for i in range(1,numRows):
            level = []
            for j in range(i-1):
                level.append(ans[i-1][j] + ans[i-1][j+1])
            ans.append([1] + level + [1])

        return ans
        # print(ans)


test = Solution()
test.generate(5)
"""
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""

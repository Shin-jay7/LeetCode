from __future__ import annotations


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        if rowIndex == 0: return [1]

        ans = [[]]

        for i in range(1,rowIndex+1):
            level = []
            for j in range(i-1):
                level.append(ans[i-1][j] + ans[i-1][j+1])
            ans.append([1] + level + [1])

        return ans[-1]
        # print(ans[-1])


test = Solution()
test.getRow(3) # [1,3,3,1]


from __future__ import annotations


class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        row = [1]

        for _ in range(rowIndex):
            row = [x+y for x,y in zip([0]+row, row+[0])]

        return row


test = Solution()
test.getRow(3) # [1,3,3,1]


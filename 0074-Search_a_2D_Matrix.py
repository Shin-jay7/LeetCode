from __future__ import annotations


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int)\
                     -> bool:
        if matrix == [] or target == None: return False

        rows, cols = len(matrix), len(matrix[0])
        lo, hi = 0, rows*cols

        while lo < hi:
            mid = (lo+hi)//2
            i, j = divmod(mid, cols)
            if matrix[i][j] == target:
                # print(True)
                # return
                return True
            elif matrix[i][j] > target:
                hi = mid
            else:
                lo = mid+1

        return False
        # print(False)


test = Solution()
test.searchMatrix([
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
], 3) # True

test = Solution()
test.searchMatrix([
  [1,   3,  5,  7],
  [10, 11, 16, 20],
  [23, 30, 34, 50]
], 13) # False

from __future__ import annotations


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        ans = []

        while matrix:
            # pop & clockwise rotation, pop & ...
            ans += matrix.pop(0)
            matrix = [*zip(*matrix)][::-1]

        # print(ans)
        return ans


test = Solution()
test.spiralOrder([
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
])
# [1,2,3,6,9,8,7,4,5]

test = Solution()
test.spiralOrder([
  [1, 2, 3, 4],
  [5, 6, 7, 8],
  [9,10,11,12]
])
[1,2,3,4,8,12,11,10,9,5,6,7]

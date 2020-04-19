from __future__ import annotations


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        if not matrix: return []
        M, N = len(matrix), len(matrix[0])
        seen = [[False]*N for _ in matrix]
        ans = []
        direc_m = [0, 1, 0, -1]
        direc_n = [1, 0, -1, 0]
        m, n, idx = 0, 0, 0

        for _ in range(M*N):
            ans.append(matrix[m][n])
            seen[m][n] = True
            next_m, next_n = m+direc_m[idx], n+direc_n[idx]
            if 0 <= next_m < M and 0 <= next_n < N and not seen[next_m][next_n]:
                m, n = next_m, next_n
            else:
                idx = (idx+1)%4
                m, n = m+direc_m[idx], n+direc_n[idx]

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

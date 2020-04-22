from __future__ import annotations


class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        ans = [[""]*n for _ in range(n)]
        seen = [[False]*n for _ in range(n)]
        r, c, num = 0, 0, 0

        for _ in range(n*n):
            while c < n and not seen[r][c]:
                num += 1
                ans[r][c] = num
                seen[r][c] = True
                c += 1
            r += 1
            c -= 1
            while r < n and not seen[r][c]:
                num += 1
                ans[r][c] = num
                seen[r][c] = True
                r += 1
            r -= 1
            c -= 1
            while 0 <= c and not seen[r][c]:
                num += 1
                ans[r][c] = num
                seen[r][c] = True
                c -= 1
            r -= 1
            c += 1
            while 0 <= r and not seen[r][c]:
                num += 1
                ans[r][c] = num
                seen[r][c] = True
                r -= 1
            r += 1
            c += 1

        # print(ans)
        return ans


test = Solution()
test.generateMatrix(0)
"""
[
 [ 1, 2, 3 ],
 [ 8, 9, 4 ],
 [ 7, 6, 5 ]
]
"""

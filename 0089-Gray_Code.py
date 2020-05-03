from __future__ import annotations

"""
https://en.wikipedia.org/wiki/Gray_code

2-bit list:     00, 01, 11, 10
Reversed:                            10, 11, 01, 00
Prefix with 0:  000, 001, 011, 010
Prefix iwth 1:                       110, 111, 101, 100
Concatenate:    000, 001, 011, 010, 110, 111, 101, 100
"""
class Solution:
    def grayCode(self, n: int) -> List[int]:
        ans = [0]

        for i in range(n):
            ans += [x | (1 << i) for x in ans[::-1]]
            """
            x | (1 << i)
            --- n = 2 ------------------
                                          00 -> [0]
            [0 | (1 << 0)] -> [0 | 1]  -> 01 -> [1]
            [1 | (1 << 1)] -> [1 | 10] -> 11 -> [3]
            [0 | (1 << 1)] -> [0 | 10] -> 10 -> [2]
            --- n = 3 ------------------
                                            000 -> [0]
            [0 | (1 << 0)] -> [0 | 1]    -> 001 -> [1]
            [1 | (1 << 1)] -> [1 | 10]   -> 011 -> [3]
            [0 | (1 << 1)] -> [0 | 10]   -> 010 -> [2]
            [2 | (1 << 2)] -> [10 | 100] -> 110 -> [6]
            [3 | (1 << 2)] -> [11 | 100] -> 111 -> [7]
            [1 | (1 << 2)] -> [1 | 100]  -> 101 -> [5]
            [0 | (1 << 2)] -> [0 | 100]  -> 100 -> [4]
            """

        return ans
        # print(ans)



test = Solution()
test.grayCode(2) # [0,1,3,2]

test = Solution()
test.grayCode(0) # [0]

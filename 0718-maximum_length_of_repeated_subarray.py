from __future__ import annotations
from typing import List


class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        # if you use str instead of chr, [11] and [1,1] become identical.
        str_nums2 = ''.join([chr(num) for num in nums2])
        str_max = ''
        cnt = 0
        for num in nums1:
            str_max += chr(num)
            if str_max in str_nums2:
                cnt = max(cnt, len(str_max))
            else:
                str_max = str_max[1:]
        return cnt


class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        m, n = len(nums1), len(nums2)        
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        cnt = 0
        for i in range(1, m+1):
            for j in range(1, n+1):
                if nums1[i-1] == nums2[j-1]:
                    dp[i][j] = 1 + dp[i-1][j-1]
                else:
                    dp[i][j] = 0
                cnt = max(cnt, dp[i][j])
        return cnt


test = Solution()
test.findLength([1,2,3,2,1], [3,2,1,4,7]) # 3

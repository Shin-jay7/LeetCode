from __future__ import annotations
from typing import List
from collections import defaultdict


class Solution:
    def fourSumCount(
        self,
        nums1: List[int], nums2: List[int],
        nums3: List[int], nums4: List[int]
      ) -> int:
        n, hash_map, ans = len(nums1), defaultdict(int), 0

        for i in range(n):
            for j in range(n):
                hash_map[nums1[i] + nums2[j]] += 1

        for k in range(n):
            for l in range(n):
                ans += hash_map[0 - (nums3[k]+nums4[l])]

        return ans

from __future__ import annotations
from typing import List


class Solution:
    def nextGreaterElement(
        self, nums1: List[int], nums2: List[int]
       ) -> List[int]:

        nges, n = [], len(nums2)
        for cur in range(n):
            nxt = cur
            while nxt < n:
                if nums2[nxt] > nums2[cur]:
                    nges.append(nums2[nxt])
                    break
                nxt += 1
            else:
                nges.append(-1)
            
        ans = []
        for num in nums1:
            ans.append(nges[nums2.index(num)])

        return ans


test = Solution()
test.nextGreaterElement([4,1,2], [1,3,4,2])

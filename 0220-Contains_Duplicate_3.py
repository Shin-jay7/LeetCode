from __future__ import annotations
from sortedcontainers import SortedList


class Solution:
    def containsNearbyAlmostDuplicate(
        self, nums: List[int], k: int, t: int
        ) -> bool:
        SList = SortedList()

        for i in range(len(nums)):
            if i > k:
                SList.remove(nums[i-k-1])
            pos1 = SortedList.bisect_left(SList, nums[i]-t)
            pos2 = SortedList.bisect_right(SList, nums[i]+t)

            if pos1 != pos2 and pos1 != len(SList):
                return True

            SList.add(nums[i])
        
        return False


test = Solution()
test.containsNearbyAlmostDuplicate([1,2,3,1], 3, 0) # True

test = Solution()
test.containsNearbyAlmostDuplicate([1,0,1,1], 1, 2) # True

test = Solution()
test.containsNearbyAlmostDuplicate([1,5,9,1,5,9], 2, 3) # False

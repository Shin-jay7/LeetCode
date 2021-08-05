from __future__ import annotations


class Solution:
    def containsNearbyAlmostDuplicate(
        self, nums: List[int], k: int, t: int
        ) -> bool:
        length = len(nums)

        for i in range(length):
            for j in range(i+1, length):
                if abs(nums[i] - nums[j]) <= t and abs(i - j) <= k:
                    return True
                    # print(True)
                    # return

        # print(False)
        return False


test = Solution()
test.containsNearbyAlmostDuplicate([1,2,3,1], 3, 0) # True

test = Solution()
test.containsNearbyAlmostDuplicate([1,0,1,1], 1, 2) # True

test = Solution()
test.containsNearbyAlmostDuplicate([1,5,9,1,5,9], 2, 3) # False

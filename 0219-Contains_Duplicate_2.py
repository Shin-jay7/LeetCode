from __future__ import annotations

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        length = len(nums)

        for i in range(length-1):
            end = i+k if length > i+k else length-1
            for j in range(end, i, -1):
                if nums[i] == nums[j]:
                    return True
                    # print(True)
                    # return
        return False
        # print(False)


test = Solution()
test.containsNearbyDuplicate([1,2,3,1], 3) # True

test = Solution()
test.containsNearbyDuplicate([1,0,1,1], 1) # True

test = Solution()
test.containsNearbyDuplicate([1,2,3,1,2,3], 2) # False

test = Solution()
test.containsNearbyDuplicate([99, 99], 2) # True

test = Solution()
test.containsNearbyDuplicate([1,2,3,4,5,6,7,8,9,9], 3) # True

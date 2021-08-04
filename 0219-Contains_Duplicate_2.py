from __future__ import annotations

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        dic = {}
        for i, v in enumerate(nums):
            if v in dic and i - dic[v] <= k:
                return True
            dic[v] = i
        return False


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

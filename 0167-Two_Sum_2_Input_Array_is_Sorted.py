from __future__ import annotations


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l, r = 0, len(numbers)-1

        while l <= r:
            sum_ = numbers[l]+numbers[r]
            if sum_ == target:
                return [l+1, r+1]
                # print([l+1, r+1])
                # return
            elif sum_ < target:
                l += 1
            else:
                r -= 1

        return []


test = Solution()
test.twoSum([2,7,11,15], 9) # [1,2]

test = Solution()
test.twoSum([2,3,4], 6) # [1,3]

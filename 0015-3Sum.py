from __future__ import annotations
import bisect

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        nums.sort()
        ans = set()

        for i in range(length-2):
            if nums[i] > 0:
                break

            l = i+1
            r = length-1
            diff = 0 - nums[i]

            while l < r:
                target = diff - nums[l]
                candidate = bisect.bisect_left(nums, target, l+1, r)

                if nums[candidate] == target:
                    ans.add((nums[i], nums[l], nums[candidate]))
                    l += 1

                    r = candidate - 1
                else:
                    l += 1

        return list(ans)

        # print(list(ans))


test = Solution()
test.threeSum([-1, 0, 1, 2, -1, -4]) # [[-1, 0, 1], [-1, -1, 2]]

test = Solution()
test.threeSum([-4,-2,1,-5,-4,-4,4,-2,0,4,0,-2,3,1,-5,0])
# [[-5,1,4],[-4,0,4],[-4,1,3],[-2,-2,4],[-2,1,1],[0,0,0]]

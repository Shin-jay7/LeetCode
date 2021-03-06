from __future__ import annotations


class Solution:
    def fourSum(self, nums: List[int], target: int) -> List[List[int]]:
        length = len(nums)
        nums.sort()
        ans = set()
        i, j = 0, 1

        for i in range(length-3):
            ### Speed up
            if nums[i] + nums[length-3] + nums[length-2] + nums[length-1] < target:
                continue
            if nums[i] + nums[i+1] + nums[i+2] + nums[i+3] > target:
                continue
            ###
            for j in range(i+1,length-2):
                ### Speed up
                if nums[i] + nums[j] + nums[length-2] + nums[length-1] < target:
                    continue
                if nums[i] + nums[j] + nums[j+1] + nums[j+2] > target:
                    continue
                ###
                l = j+1
                r = length-1

                while l < r:
                    total = nums[i] + nums[j] + nums[l] + nums[r]
                    if total == target:
                        ans.add((nums[i], nums[j], nums[l], nums[r]))
                        l += 1
                    elif total > target:
                        r -= 1
                    else:
                        l += 1

        return list(ans)
        # print(list(ans))


test = Solution()
test.fourSum([1, 0, -1, 0, -2, 2], 0)
# [[-1, 0, 0, 1], [-2, -1, 1, 2], [-2, 0, 0, 2]]

test = Solution()
test.fourSum([-3,-2,-1,0,0,1,2,3], 0)
#[
# [-3,-2,2,3],[-3,-1,1,3],[-3,0,0,3],
# [-3,0,1,2],[-2,-1,0,3],[-2,-1,1,2],
# [-2,0,0,2],[-1,0,0,1]
#]




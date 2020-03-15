from __future__ import annotations

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        length = len(nums)
        nums.sort()
        ans = set()

        for i in range(length-2):
            l = i+1
            r = length-1

            while l < r:
                if nums[i] + nums[l] + nums[r] == 0:
                    ans.add((nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1
                elif nums[i] + nums[l] + nums[r] < 0:
                    l += 1
                else:
                    r -= 1

        return list(ans)

        # print(list(ans))


test = Solution()
test.threeSum([-1, 0, 1, 2, -1, -4]) # [[-1, 0, 1], [-1, -1, 2]]

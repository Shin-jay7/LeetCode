from __future__ import annotations

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

            while l < r:
                total = nums[i] + nums[l] + nums[r]
                if total == 0:
                    ans.add((nums[i], nums[l], nums[r]))
                    l += 1
                    r -= 1
                elif total < 0:
                    l += 1
                else:
                    r -= 1

        return list(ans)

        # print(list(ans))


test = Solution()
test.threeSum([-1, 0, 1, 2, -1, -4]) # [[-1, 0, 1], [-1, -1, 2]]

test = Solution()
test.threeSum([-4,-2,1,-5,-4,-4,4,-2,0,4,0,-2,3,1,-5,0])
# [[-5,1,4],[-4,0,4],[-4,1,3],[-2,-2,4],[-2,1,1],[0,0,0]]

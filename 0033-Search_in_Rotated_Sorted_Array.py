from __future__ import annotations


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums)
        while lo < hi:
            mid = (lo+hi)//2
            if (nums[mid] < nums[0]) == (target < nums[0]):
                if nums[mid] < target:
                    lo = mid + 1
                elif nums[mid] > target:
                    hi = mid
                else:
                    return mid
                    # print(mid)
                    # return
            elif target < nums[0]:
                lo = mid + 1
            else:
                hi = mid

        # print(-1)
        return -1


test = Solution()
test.search([4,5,6,7,0,1,2], 0) # 4

test = Solution()
test.search([4,5,6,7,0,1,2], 3) # -1

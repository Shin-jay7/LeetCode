from __future__ import annotations


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums)-1

        while lo <= hi:
            mid = (lo+hi+1)//2
            if nums[mid] == target:
                return mid
                # print(mid)
                # return
            # the first half is ordered = mid is in the first half
            if nums[lo] <= nums[mid]:
                # target is in the first half
                if nums[lo] <= target < nums[mid]:
                    hi = mid-1
                else:
                    lo = mid+1
            # the second half is ordered = mid is in the second half
            else:
                # target is in the second half
                if nums[mid] < target <= nums[hi]:
                    lo = mid+1
                else:
                    hi = mid-1

        return -1
        # print(-1)


test = Solution()
test.search([4,5,6,7,0,1,2], 0) # 4

test = Solution()
test.search([4,5,6,7,0,1,2], 3) # -1

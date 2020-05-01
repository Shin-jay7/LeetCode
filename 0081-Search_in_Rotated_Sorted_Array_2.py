from __future__ import annotations


class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        lo, hi = 0, len(nums)-1

        while lo <= hi:
            mid = (lo+hi+1)//2
            if nums[mid] == target:
                return True
                # print(True)
                # return
            # handle tricky case
            while lo < mid and nums[lo] == nums[mid]:
                lo += 1
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

        return False
        # print(False)
        # return


test = Solution()
test.search([1,3,1,1], 3) # True

test = Solution()
test.search([2,5,6,0,0,1,2], 0) # True

test = Solution()
test.search([2,5,6,0,0,1,2], 3) # False

test = Solution()
test.search([4,5,6,7,0,1,2], 0) # True

test = Solution()
test.search([4,5,6,7,0,1,2], 3) # False

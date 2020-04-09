from __future__ import annotations


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        i, count = 0, 1
        l = len(nums)

        while i < l:
            num = nums[i]
            if 1 <= num < l and nums[num-1] != nums[i]:
                nums[num-1], nums[i] = nums[i], nums[num-1]
                # print(nums)
            else:
                i += 1
                # print(i)
                while count-1 < l and nums[count-1] == count:
                    count += 1
                # print(count)

        return count


test = Solution()
test.firstMissingPositive([1,2,0]) # 3

test = Solution()
test.firstMissingPositive([3,4,-1,1]) # 2

# test = Solution()
# test.firstMissingPositive([7,8,9,11,12]) # 1

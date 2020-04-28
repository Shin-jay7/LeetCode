from __future__ import annotations


class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        carry = 1
        for i in range(len(digits)-1,-1,-1):
            carry, num = divmod(digits[i]+carry, 10)
            digits[i] = num

        if carry:
            digits = [carry] + digits

        return digits
        # print(digits)


test = Solution()
test.plusOne([1,2,3]) # [1,2,4]

test = Solution()
test.plusOne([4, 3, 2, 1]) # [4, 3, 2, 2]

test = Solution()
test.plusOne([9, 9, 9]) # [1, 0, 0, 0]

test = Solution()
test.plusOne([0]) # [1]


from __future__ import annotations


class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x%10 == 0 and x != 0):
            return False

        revertedNum = 0

        while x > revertedNum:
            revertedNum = revertedNum*10 + x%10
            x //= 10

        return x == revertedNum or x == revertedNum//10


test = Solution()
test.isPalindrome(11) # True

test = Solution()
test.isPalindrome(121) # True

test = Solution()
test.isPalindrome(-121) # False

test = Solution()
test.isPalindrome(10) # False

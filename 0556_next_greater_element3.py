from __future__ import annotations


# https://leetcode.com/problems/next-greater-element-iii/discuss/983076/Python-O(m)-solution-explained
class Solution:
    def nextGreaterElement(self, n: int) -> int:
        digits = list(str(n))
        i = len(digits) - 1
        while i-1 >= 0 and digits[i] <= digits[i-1]:
            i -= 1
        if i == 0:
            return -1
        j = i
        while j + 1 < len(digits) and digits[j+1] > digits[i-1]:
            j += 1
        digits[i-1], digits[j] = digits[j], digits[i-1]
        digits[i:] = digits[i:][::-1]
        ans = int(''.join(digits))

        return ans if ans < 2 ** 31 else -1


test = Solution()
test.nextGreaterElement(12)  # 21

test = Solution()
test.nextGreaterElement(21)  # -1

test = Solution()
test.nextGreaterElement(112)  # 121

test = Solution()
test.nextGreaterElement(230241)  # 230412

test = Solution()
test.nextGreaterElement(2147483486)  # -1

test = Solution()
test.nextGreaterElement(2147483476)  # 2147483647

test = Solution()
test.nextGreaterElement(101)  # 110

from __future__ import annotations


class Solution:
    def checkValidString(self, s: str) -> bool:
        # _max: the maximum number of open left parenthesis that could be
        #       matched with right parenthesis.
        # _min: the minimum number of open left parenthesis that must be
        #       matched with right parenthesis.
        _max, _min = 0, 0
        for char in s:
            if char == "(":
                _max += 1
                _min += 1
            if char == ")":
                _max -= 1
                _min = max(_min-1, 0)
            if char == "*":
                _max += 1
                _min = max(_min-1, 0)
            if _max < 0:
                return False
        return _min == 0


test = Solution()
test.checkValidString("()") # True

test = Solution()
test.checkValidString("(*)") # True

test = Solution()
test.checkValidString("(*))") # True

test = Solution()
test.checkValidString("**))") # True

test = Solution()
test.checkValidString("(") # False
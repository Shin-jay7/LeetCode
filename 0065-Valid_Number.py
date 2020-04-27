from __future__ import annotations
import re


class Solution:
    def isNumber(self, s: str) -> bool:
        s = s.strip()
        found_dot = found_e = found_digit = False

        for i, char in enumerate(s):
            if char in "+-":
                if i > 0 and s[i-1] != "e":
                    return False
            elif char == ".":
                if found_dot or found_e:
                    return False
                found_dot = True
            elif char == "e":
                if found_e or not found_digit:
                    return False
                found_e, found_digit = True, False
            elif char in "0123456789":
                found_digit = True
            else:
                return False

        return found_digit


test = Solution()
test.isNumber("0") # True

test = Solution()
test.isNumber(" 0.1 ") # True

test = Solution()
test.isNumber("abc") # False

test = Solution()
test.isNumber("1 a") # False

test = Solution()
test.isNumber("2e10") # True

test = Solution()
test.isNumber(" -90e3   ") # True

test = Solution()
test.isNumber(" 1e") # False

test = Solution()
test.isNumber("e3") # False

test = Solution()
test.isNumber(" 6e-1") # True

test = Solution()
test.isNumber(" 99e2.5 ") # False

test = Solution()
test.isNumber("53.5e93") # True

test = Solution()
test.isNumber(" --6 ") # False

test = Solution()
test.isNumber("-+3") # False

test = Solution()
test.isNumber("95a54e53") # False

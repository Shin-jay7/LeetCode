from __future__ import annotations
import re


class Solution:
    def isNumber(self, s: str) -> bool:
        states = [{},
                  # state(1): initial state
                  {"blank": 1, "sign": 2, "digit": 3, ".": 4},
                  # state(2): found sign
                  {"digit": 3, ".": 4},
                  # state(3): digit consumer (loop until non-digit)
                  {"digit": 3, ".": 5, "e": 6, "blank": 9},
                  # state(4): found dot (only a digit is valid)
                  {"digit": 5},
                  # state(5): after dot (expect digits, e or end of valid input)
                  {"digit": 5, "e": 6, "blank": 9},
                  # state(6): found "e" (only sign or digit valid)
                  {"sign": 7, "digit": 8},
                  # state(7): sign after "e" (only digit)
                  {"digit": 8},
                  # state(8): digit after "e" (expect digits or end of valid input)
                  {"digit": 8, "blank": 9},
                  # state(9): terminal state (fail if non-blank found)
                  {"blank": 9}
        ]

        currentState = 1

        for c in s:
            if c in "0123456789":
                c = "digit"
            elif c in " \t\n":
                c = "blank"
            elif c in "+-":
                c = "sign"

            if c not in states[currentState]:
                return False

            currentState = states[currentState][c]

        if currentState not in [3, 5, 8, 9]:
            return False

        return True


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

from __future__ import annotations


class Solution:
    def isNumber(self, s: str) -> bool:
        states = [
            {" ": 0, "sign": 1, "digit": 2, ".": 3},
            {"digit": 2, ".": 3},
            {"digit": 2, ".": 4, "e": 5, " ": 8},
            {"digit": 4},
            {"digit": 4, "e": 5, " ": 8},
            {"sign": 6, "digit": 7},
            {"digit": 7},
            {"digit": 7, " ": 8},
            {" ": 8}
        ]

        cur = 0

        for char in s:
            if char in "+-":
                char = "sign"
            elif char in "0123456789":
                char = "digit"

            if char not in states[cur]:
                return False

            cur = states[cur][char]

        return cur in [2,4,7,8]



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

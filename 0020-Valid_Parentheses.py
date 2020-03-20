from __future__ import annotations


class Solution:
    def isValid(self, strings: str) -> bool:
        remaining_brackets = ""
        bracket_pairs = {
            ")": "(",
            "]": "[",
            "}": "{"
        }

        for s in strings:
            if s == ")" or s == "]" or s == "}":
                if remaining_brackets != "" and\
                   remaining_brackets[-1] == bracket_pairs[s]:
                    remaining_brackets = remaining_brackets[:-1]
                else:
                    return False
            else:
                remaining_brackets += s

        return remaining_brackets == ""


test = Solution()
test.isValid("()") # True

test = Solution()
test.isValid("()[]{}") # True

test = Solution()
test.isValid("(]") # False

test = Solution()
test.isValid("([)]") # False

test = Solution()
test.isValid("{[]}") # True

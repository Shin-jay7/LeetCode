from __future__ import annotations


class Solution:
    def isValid(self, strings: str) -> bool:
        round_brackets, square_brackets, curly_brackets = 0, 0, 0

        remaining_brackets = ""

        for idx,s in enumerate(strings):
            if s == ")" and remaining_brackets != "":
                if remaining_brackets[-1] == "(":
                    remaining_brackets = remaining_brackets[:-1]
                else:
                    # print(False)
                    # return
                    return False
            elif s == "]" and remaining_brackets != "":
                if remaining_brackets[-1] == "[":
                    remaining_brackets = remaining_brackets[:-1]
                else:
                    # print(False)
                    # return
                    return False
            elif s == "}" and remaining_brackets != "":
                if remaining_brackets[-1] == "{":
                    remaining_brackets = remaining_brackets[:-1]
                else:
                    # print(False)
                    # return
                    return False
            else:
                remaining_brackets += s

        # print(remaining_brackets == "")
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

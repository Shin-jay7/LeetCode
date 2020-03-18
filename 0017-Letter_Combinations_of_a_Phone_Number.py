from __future__ import annotations


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        letterList = {
            "2": ["a", "b", "c"],
            "3": ["d", "e", "f"],
            "4": ["g", "h", "i"],
            "5": ["j", "k", "l"],
            "6": ["m", "n", "o"],
            "7": ["p", "q", "r", "s"],
            "8": ["t", "u", "v"],
            "9": ["w", "x", "y", "z"]
        }
        ans = []

        def combineHelper(combination, remaining_digits):
            if len(remaining_digits) == 0:
                ans.append(combination)
            else:
                for letter in letterList[remaining_digits[0]]:
                    combineHelper(combination+letter, remaining_digits[1:])

        if digits:
            combineHelper("", digits)

        return ans


test = Solution()
test.letterCombinations("23") # ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"]

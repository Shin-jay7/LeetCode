from __future__ import annotations
import re


class Solution:
    def romanToInt(self, s: str) -> int:
        ans = 0
        intDict = {
            "M": 1000,
            "CM": 900,
            "D": 500,
            "CD": 400,
            "C": 100,
            "XC": 90,
            "L": 50,
            "XL": 40,
            "X": 10,
            "IX": 9,
            "V": 5,
            "IV": 4,
            "I": 1
        }
        for key in intDict.keys():
            while re.match(key, s):
                ans += intDict[key]
                s = s[len(key):]

        return ans


test = Solution()
test.romanToInt("III") # 3

test = Solution()
test.romanToInt("IV") # 4

test = Solution()
test.romanToInt("IX") # 9

test = Solution()
test.romanToInt("LVIII") # 58

test = Solution()
test.romanToInt("MCMXCIV") # 1994

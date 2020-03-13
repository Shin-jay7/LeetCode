from __future__ import annotations


class Solution:
    def romanToInt(self, s: str) -> int:
        ans = 0
        intDict = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000
        }
        result, ans = [], 0
        for letter in s:
            result.append(intDict[letter])
        for i in range(len(result)-1):
            if result[i+1] > result[i]:
                ans -= result[i]
            else:
                ans += result[i]
        ans += result[-1]

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

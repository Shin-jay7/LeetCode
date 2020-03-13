from __future__ import annotations


class Solution:
    def intToRoman(self, num: int) -> str:
        ans = ""
        romanDict = {
            1000: "M",
            900: "CM",
            500: "D",
            400: "CD",
            100: "C",
            90: "XC",
            50: "L",
            40: "XL",
            10: "X",
            9: "IX",
            5: "V",
            4: "IV",
            1: "I"
        }
        for key in romanDict.keys():
            q, num = divmod(num, key)
            ans += q*romanDict[key]

        return ans

        # Runtime: key/value dict (52ms), list(56ms)

        # for i in [[1000, "M"], [900, "CM"],[500, "D"], [400, "CD"], [100, "C"], [90, "XC"], [50, "L"], [40, "XL"], [10, "X"], [9, "IX"], [5, "V"], [4, "IV"], [1, "I"]]:
            # q, num = divmod(num, i[0])
            # ans += q*i[1]

test = Solution()
test.intToRoman(3) # "III"

test = Solution()
test.intToRoman(4) # "IV"

test = Solution()
test.intToRoman(9) # "IX"

test = Solution()
test.intToRoman(58) # "LVIII"

test = Solution()
test.intToRoman(1994) # "MCMXCIV"


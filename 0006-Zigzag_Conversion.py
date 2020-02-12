from __future__ import annotations


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        pos, mov = 0, 1
        columns = [""] * numRows
        ans = ""

        for i in range(len(s)):
            columns[pos] += s[i]
            if numRows > 1:
                pos += mov
                if pos == 0 or pos == numRows-1:
                    mov *= -1

        for j in range(numRows):
            ans += columns[j]

        return ans


test = Solution()
test.convert("Apalindromeisaword,phrase,number,orothersequenceofunitsthatcanbereadthesamewayineitherdirection,withgeneralallowancesforadjustmentstopunctuationandworddividers.", 4)

test = Solution()
test.convert("PAYPALISHIRING", 5) # "PHASIYIRPLIGAN"

test = Solution()
test.convert("ABCDE", 4) # "ABCED"

test = Solution()
test.convert("AB", 1) # "AB"

test = Solution()
test.convert("A", 1) # "A"

test = Solution()
test.convert("", 1) # ""

test = Solution()
test.convert("ABC", 2) # "ACB"

test = Solution()
test.convert("PAYPALISHIRI", 3) # "PAHAPLSIIYIR"

test = Solution()
test.convert("PAYPALISHIRING", 3) # "PAHNAPLSIIGYIR"

test = Solution()
test.convert("PAYPALISHIRING", 4) # "PINALSIGYAHRPI"


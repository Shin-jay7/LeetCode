from __future__ import annotations


class Solution:
    def convert(self, s: str, numRows: int) -> str:
        length = len(s)
        dgnl = min(numRows-2, length-numRows)

        if length <= numRows or dgnl < 0:
            return s

        q, mod = divmod(length, numRows+dgnl)
        if mod == 0:
            modColumns = 0
        elif mod <= numRows:
            modColumns = 1
        else:
            modColumns = 1 + (mod-numRows)
        numColumns = q*(1+dgnl) + modColumns
        matrix = [[" "]*numRows for _ in range(numColumns)]

        for i in range(0,numColumns,dgnl+1):
            matrix[i] = list(s[:numRows])
            addon = numRows - len(matrix[i])
            if addon:
                matrix[i] += " " * addon
                break
            s = s[numRows:]
            if s == "":
                break

            for j in range(1,dgnl+1):
                matrix[i+j][numRows-(j+1)] = s[0]
                s = s[1:]
                if s == "":
                    break

        trs = [[matrix[j][i] for j in range(len(matrix))] for i in range(len(matrix[0]))]
        return ''.join(''.join(_) for _ in trs).replace(" ","")


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


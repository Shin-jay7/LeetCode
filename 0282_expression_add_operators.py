from __future__ import annotations
from typing import List


class Solution:
    def addOperators(self, num: str, target: int) -> List[str]:
        ans = []

        def backtracking(i=0, prefix='', value=0, prev=0):
            if i == len(num) and value == target:
                ans.append(prefix)
                return

            for j in range(i+1, len(num)+1):
                string = num[i:j]
                number = int(string)
                if string != '0' and num[i] == '0':
                    continue
                if not prefix:
                    backtracking(j, string, number, number)
                else:
                    backtracking(j, prefix + '+' + string, value + number, number)
                    backtracking(j, prefix + '-' + string, value - number, -number)
                    backtracking(j, prefix + '*' + string, value - prev + prev * number, prev * number)
        
        backtracking()
        return ans

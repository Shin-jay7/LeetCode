from __future__ import annotations
import collections

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        seq = collections.defaultdict(int)
        for i in range(len(s)-9):
            seq[s[i:i+10]] += 1

        return [key for key, value in seq.items() if value > 1]
        # print([key for key, value in seq.items() if value > 1])

test = Solution()
test.findRepeatedDnaSequences("AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT") 
# ["AAAAACCCCC","CCCCCAAAAA"] 

test = Solution()
test.findRepeatedDnaSequences("AAAAAAAAAAAAA") # ["AAAAAAAAAA"]
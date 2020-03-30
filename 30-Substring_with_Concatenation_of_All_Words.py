from __future__ import annotations
from collections import Counter


class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if not s or not words:
            return []

        w_map = Counter(words)
        w_len = len(words[0])
        w_num = len(words)
        l_len = w_len*w_num
        s_len = len(s)
        ans = []

        for i in range(s_len-l_len+1):
            seen = dict(w_map)
            w_used = 0
            for j in range(i, i+l_len, w_len):
                w = s[j:j+w_len]
                if w in seen and seen[w] > 0:
                    seen[w] -= 1
                    w_used += 1
                else:
                    break
            if w_used == w_num:
                ans.append(i)

        return ans


test = Solution()
test.findSubstring("barfoothefoobarman", ["foo","bar"])
# [0,9]

test = Solution()
test.findSubstring("wordgoodgoodgoodbestwordn",\
                   ["word","good","best","word"])
# []

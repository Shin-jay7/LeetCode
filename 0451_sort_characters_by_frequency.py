from __future__ import annotations
from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        ans = ""
        for char, freq in Counter(s).most_common():
            ans += char * freq

        return ans


test = Solution()
test.frequencySort("tree") # "eert"

test = Solution()
test.frequencySort("cccaaa") # "aaaccc"

test = Solution()
test.frequencySort("Aabb") # "bbAa"

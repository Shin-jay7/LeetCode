from __future__ import annotations
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        dic = defaultdict(list)

        for word in strs:
            sorted_w = "".join(sorted(word))
            dic[sorted_w].append(word)

        for key in dic.keys():
            anagram = []
            for word in dic[key]:
                anagram.append(word)
            ans.append(anagram)

        # print(ans)
        return ans


test = Solution()
test.groupAnagrams( ["eat", "tea", "tan", "ate", "nat", "bat"])
"""
[
  ["ate","eat","tea"],
  ["nat","tan"],
  ["bat"]
]
"""

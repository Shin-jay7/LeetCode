from __future__ import annotations
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = []
        dic = defaultdict(list)

        for idx,word in enumerate(strs):
            sorted_w = "".join(sorted(word))
            dic[sorted_w].append(idx)

        for key in dic.keys():
            anagram = []
            for val in dic[key]:
                anagram.append(strs[val])
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

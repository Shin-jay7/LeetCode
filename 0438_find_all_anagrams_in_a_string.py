from __future__ import annotations
from collections import defaultdict
from typing import List
import string


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        hashmap = defaultdict(int)
        ans, s_len, p_len = [], len(s), len(p)
        if p_len > s_len:
            return []

        for ch in p:
            hashmap[ch] += 1
        for i in range(p_len-1):
            if s[i] in hashmap:
                hashmap[s[i]] -= 1
        for i in range(-1, s_len-p_len+1):
            if i > -1 and s[i] in hashmap:
                hashmap[s[i]] += 1
            if i+p_len < s_len and s[i+p_len] in hashmap:
                hashmap[s[i+p_len]] -= 1
            if all(v == 0 for v in hashmap.values()):
                ans.append(i+1)

        return ans


# https://leetcode.com/problems/find-all-anagrams-in-a-string/discuss/1738052/A-very-deep-EXPLANATION-oror-Solved-without-using-HashTable
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans, s_len, p_len = [], len(s), len(p)
        if p_len > s_len:
            return []
        s_list, p_list = [0]*26, [0]*26

        for ch in p:
            idx = string.ascii_lowercase.index(ch)
            p_list[idx] += 1

        left, right = 0, p_len
        while right < s_len+1:
            for i in range(p_len):
                idx = string.ascii_lowercase.index(s[left+i])
                s_list[idx] += 1
            if p_list == s_list:
                ans.append(left)
            left += 1
            right += 1
            s_list = [0]*26
                
        return ans

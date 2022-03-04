from __future__ import annotations
from typing import List
import string


# https://leetcode.com/problems/find-all-anagrams-in-a-string/discuss/1738052/A-very-deep-EXPLANATION-oror-Solved-without-using-HashTable
class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans, s_len, p_len = [], len(s), len(p)
        if p_len > s_len:
            return []
        s_list, p_list = [0]*26, [0]*26

        for char in p:
            idx = string.ascii_lowercase.index(char)
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

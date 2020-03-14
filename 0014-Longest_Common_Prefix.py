from __future__ import annotations


class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        prefix = ""
        if strs == []:
            return prefix

        for idx,letter in enumerate(min(strs, key=len)):
            for str in strs:
                if letter != str[idx]:
                    return prefix
            prefix += letter

        return prefix


test = Solution()
test.longestCommonPrefix(["flower","flow","flight"]) # "fl"

test = Solution()
test.longestCommonPrefix(["dog","racecar","car"]) # ""

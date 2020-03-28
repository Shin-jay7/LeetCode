from __future__ import annotations


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        for i in range(len(haystack)-len(needle)+1):
            if haystack[i:i+len(needle)] == needle:
                return i

        return -1


test = Solution()
test.strStr("babba", "bbb") # -1

test = Solution()
test.strStr("aaa", "aaa") # 0

test = Solution()
test.strStr("aaa", "a") # 0

test = Solution()
test.strStr("mississippi", "issip") # 4

test = Solution()
test.strStr("hello", "ll") # 2

test = Solution()
test.strStr("helollo", "ll") # 4

test = Solution()
test.strStr("helolo", "ll") # -1

test = Solution()
test.strStr("aaaaa", "bba") # -1

test = Solution()
test.strStr("aaaaa", "") # 0

test = Solution()
test.strStr("", "ll") # -1

test = Solution()
test.strStr("", "") # 0

test = Solution()
test.strStr("aaa", "aaaa") # -1

test = Solution()
test.strStr("a", "a") # 0

from __future__ import annotations


class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        return sorted(s) == sorted(t)
        # print(sorted(s) == sorted(t))


test = Solution()
test.isAnagram("anagram", "nagaram") # True

test = Solution()
test.isAnagram("rat", "car") # False

from __future__ import annotations


class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        for char in set(s):
            if s.count(char) < k:
                return max(
                    self.longestSubstring(subs, k) for subs in s.split(char))
        return len(s)


test = Solution()
test.longestSubstring("aaabb", 3) # 3

test = Solution()
test.longestSubstring("ababbc", 2) # 5

test = Solution()
test.longestSubstring("aaabbb", 3) # 6

test = Solution()
test.longestSubstring("weitong", 2) # 0

test = Solution()
test.longestSubstring("ababacb", 3) # 0

test = Solution()
test.longestSubstring("bbaaacbd", 3) # 3

from __future__ import annotations


# https://leetcode.com/problems/longest-repeating-character-replacement/discuss/765776/Python%3A-Two-Pointers-%2B-Process-for-coding-interviews
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left, freq, longest = 0, {}, 0

        for right in range(len(s)):
            if not s[right] in freq:
                freq[s[right]] = 0
            freq[s[right]] += 1
            cnt = right - left + 1
            if cnt - max(freq.values()) <= k:
                longest = max(longest, cnt)
            else:
                freq[s[left]] -= 1
                if not freq[s[left]]:
                    freq.pop(s[left])
                left += 1

        return longest

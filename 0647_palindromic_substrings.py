from __future__ import annotations


# class Solution:
#     def countSubstrings(self, s: str) -> int:
#         ans = 0
#         for sub in [s[i:j]
#                     for i in range(len(s))
#                     for j in range(i+1, len(s)+1)]:
#             if sub == sub[::-1]:
#                 ans += 1
#         return ans


class Solution:
    def countSubstrings(self, s: str) -> int:
        ans = 0
        for i in range(2*len(s)-1):
            left = i // 2
            right = (i+1) // 2
            while left >= 0 and right < len(s) and s[left] == s[right]:
                ans += 1
                left -= 1
                right += 1
        return ans


test = Solution()
test.countSubstrings("abc")  # 3

test = Solution()
test.countSubstrings("aaa")  # 6

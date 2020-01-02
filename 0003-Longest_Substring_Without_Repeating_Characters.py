# original: 0.118911507
# Brute force: 0.617322538

from __future__ import annotations


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        max_ = 0
        for i in range(n):
            for j in range(i+1, n+1):
                if allUnique(s, i, j):
                    max_ = max(max_, j-i)

        return max_

def allUnique(s: str, start: int, end: int) -> bool:
    range_ = s[start:end]
    return True if len(range_) == len(set(range_)) else False


test = Solution()
test.lengthOfLongestSubstring("abcabcbb") # 3
test.lengthOfLongestSubstring("bbbbb") # 1
test.lengthOfLongestSubstring("pwwkew") # 3
test.lengthOfLongestSubstring(" ") # 1
test.lengthOfLongestSubstring("") # 0
test.lengthOfLongestSubstring("au") # 2


# import timeit

# code = """
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         n = len(s)
#         max_ = 0
#         for i in range(n):
#             for j in range(i+1, n+1):
#                 if allUnique(s, i, j):
#                     max_ = max(max_, j-i)

#         return max_

# def allUnique(s: str, start: int, end: int) -> bool:
#     range_ = s[start:end]
#     return True if len(range_) == len(set(range_)) else False

# test = Solution()
# test.lengthOfLongestSubstring("abcabcbb") # 3
# test.lengthOfLongestSubstring("bbbbb") # 1
# test.lengthOfLongestSubstring("pwwkew") # 3
# test.lengthOfLongestSubstring(" ") # 1
# test.lengthOfLongestSubstring("") # 0
# test.lengthOfLongestSubstring("au") # 2
# """

# print(timeit.timeit(code, number=10000))

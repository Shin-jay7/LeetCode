# original: 0.118911507
# Brute force: 0.617322538
# Sliding window: 0.162572
# Sliding window2: 0.12389086299999999
# Sliding window3: 0.153267076

from __future__ import annotations


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        dictionary = {}
        max_, i, j = 0, 0, 0
        while i < n and j < n:
            if s[j] in dictionary.keys():
                i = max(i, dictionary[s[j]]+1)
            max_ = max(max_, j-i+1)
            dictionary[s[j]] = j
            j += 1

        return max_


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
#         dictionary = {}
#         max_, i, j = 0, 0, 0
#         while i < n and j < n:
#             if s[j] in dictionary.keys():
#                 i = max(i, dictionary[s[j]]+1)
#             max_ = max(max_, j-i+1)
#             dictionary[s[j]] = j
#             j += 1

#         return max_

# test = Solution()
# test.lengthOfLongestSubstring("abcabcbb") # 3
# test.lengthOfLongestSubstring("bbbbb") # 1
# test.lengthOfLongestSubstring("pwwkew") # 3
# test.lengthOfLongestSubstring(" ") # 1
# test.lengthOfLongestSubstring("") # 0
# """

# print(timeit.timeit(code, number=10000))

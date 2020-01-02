# original: 0.118911507
# Brute force: 0.617322538
# Sliding window: 0.162572

from __future__ import annotations


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        unique_list = []
        max_, i, j = 0, 0, 0
        while (i < n and j < n):
            if s[j] not in unique_list:
                unique_list.append(s[j])
                max_ = max(max_, j-i+1)
                j += 1
            else:
                unique_list = unique_list[1:]
                i += 1

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
#         unique_list = []
#         max_, i, j = 0, 0, 0
#         while (i < n and j < n):
#             if s[j] not in unique_list:
#                 unique_list.append(s[j])
#                 max_ = max(max_, j-i+1)
#                 j += 1
#             else:
#                 unique_list = unique_list[1::]
#                 i += 1

#         return max_

# test = Solution()
# test.lengthOfLongestSubstring("abcabcbb") # 3
# test.lengthOfLongestSubstring("bbbbb") # 1
# test.lengthOfLongestSubstring("pwwkew") # 3
# test.lengthOfLongestSubstring(" ") # 1
# test.lengthOfLongestSubstring("") # 0
# test.lengthOfLongestSubstring("au") # 2
# """

# print(timeit.timeit(code, number=10000))

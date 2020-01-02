from __future__ import annotations


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_ = 0
        for i in range(len(s)):
            unique_list = [s[i]]
            for j in range(i+1, len(s)):
                if s[j] not in unique_list:
                    unique_list.append(s[j])
                else:
                    max_ = max(max_, len(unique_list))

        return max_


# import timeit

# code = """
# class Solution:
#     def lengthOfLongestSubstring(self, s) -> int:
#         max_ = 0
#         for i in range(len(s)):
#             unique_list = [s[i]]
#             for j in range(i+1, len(s)):
#                 if s[j] not in unique_list:
#                     unique_list.append(s[j])
#                 else:
#                     max_ = max(max_, len(unique_list))

#         return max_

# test = Solution()
# test.lengthOfLongestSubstring("abcabcbb")
# """

# print(timeit.timeit(code, number=10000))

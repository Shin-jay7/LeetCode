from __future__ import annotations


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        max_ = 0
        for i in range(len(s)):
            unique_list = [s[i]]
            max_ = max(max_, len(unique_list))
            for j in range(i+1, len(s)):
                if s[j] not in unique_list:
                    unique_list.append(s[j])
                    max_ = max(max_, len(unique_list))
                else:
                    max_ = max(max_, len(unique_list))
                    break

        return max_


test = Solution()
test.lengthOfLongestSubstring("abcabcbb") # 3
# test.lengthOfLongestSubstring("bbbbb") # 1
# test.lengthOfLongestSubstring("pwwkew") # 3
# test.lengthOfLongestSubstring(" ") # 1
# test.lengthOfLongestSubstring("") # 0
# test.lengthOfLongestSubstring("au") # 2


# import timeit

# code = """
#
#
# test = Solution()
# test.lengthOfLongestSubstring("abcabcbb")
# """

# print(timeit.timeit(code, number=10000))

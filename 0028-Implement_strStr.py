from __future__ import annotations


class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        h_length = len(haystack)
        n_length = len(needle)

        if needle == "":
            # print(0)
            # return
            return 0
        elif haystack == "" or h_length < n_length:
            # print(-1)
            # return
            return -1

        h, n, start_idx, checking = 0, 0, 0, 0

        while h < h_length:
            if haystack[h] == needle[n]:
                if n == n_length-1:
                    # print(start_idx)
                    # return
                    return start_idx
                elif checking == 0:
                    start_idx = h
                    checking = 1
                n += 1
            elif checking == 1:
                h = start_idx
                n = 0
                checking = 0
                start_idx = -1
            h += 1

        return -1
        # print(-1)


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

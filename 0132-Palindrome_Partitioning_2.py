from __future__ import annotations


class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)

        # Speed up for simple cases
        if s == s[::-1]: return 0
        for i in range(1,n):
            if s[:i] == s[:i][::-1] and s[i:] == s[i:][::-1]:
                return 1

        # Num of cuts required for each s length in the worst case
        cut = list(range(-1,n))

        for i in range(n):
            # use i as origin, and gradually enlarge radius
            # if a palindrome exists
            radO, radE = 0, 0
            # Odd palindrome
            while i-radO >= 0 and i+radO < n and\
                  s[i-radO] == s[i+radO]:
                cut[i+radO+1] = min(cut[i+radO+1], cut[i-radO]+1)
                radO += 1
            # Even palindrome
            while i-radE >= 0 and i+radE+1 < n and\
                  s[i-radE] == s[i+radE+1]:
                cut[i+radE+2] = min(cut[i+radE+2], cut[i-radE]+1)
                radE += 1

        # print(cut[-1])
        return cut[-1]


# Shorter version with the same speed
class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)

        if s == s[::-1]: return 0
        for i in range(1,n):
            if s[:i] == s[:i][::-1] and s[i:] == s[i:][::-1]:
                return 1

        cut = list(range(-1,n))

        for idx in range(n):
            for l, r in (idx,idx), (idx-1,idx):
                # gradually enlarge radius if a palindrome exists
                while l >=0 and r < n and s[l] == s[r]:
                    cut[r+1] = min(cut[r+1], cut[l]+1)
                    l -= 1
                    r += 1

        # print(cut[-1])
        return cut[-1]


test = Solution()
test.minCut("aab")
# The palindrome partitioning ["aa","b"] could be produced using 1 cut.

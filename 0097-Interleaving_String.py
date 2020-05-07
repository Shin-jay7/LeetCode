from __future__ import annotations
from timeit import timeit
from functools import partial


"""
Given three strings A, B and C. Write a function that checks
whether C is an interleaving of A and B. C is said to be
interleaving A and B, if it contains all characters of A and B
and order of all characters in individual strings is preserved.

For example:

'hotdog' is an interleaving of 'hot' and 'dog' (easy)
'superb' is an interleaving of 'up' and 'serb'
'cheaters' is not an interleaving of 'chat' and 'seer',
because while it contains all the letters from each,
the letters from 'seer' do not appear in order
"""

"""
s3=hotdog
           O(m*n):  0.000006 seconds
           O(2*n):  0.000004 seconds
             O(n):  0.000003 seconds
              DFS:  0.000003 seconds
              BFS:  0.000003 seconds

s3=aadbbcbcacefghilmnopjkqr
           O(m*n):  0.000042 seconds
           O(2*n):  0.000036 seconds
             O(n):  0.000025 seconds
              DFS:  0.000019 seconds
              BFS:  0.000025 seconds

s3=hotdog
           O(m*n):  0.000009 seconds
           O(2*n):  0.000006 seconds
             O(n):  0.000007 seconds
              DFS:  0.000007 seconds
              BFS:  0.000007 seconds
"""

solutions = []

class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        r, c, l = len(s1), len(s2), len(s3)
        if r + c != l: return False

        # Require 0 range for no strings of s1 or/and s2
        dp = [[True for _ in range(c+1)] for _ in range(r+1)]

        for i in range(1, r+1):
            dp[i][0] = dp[i-1][0] and s1[i-1] == s3[i-1]
        for j in range(1, c+1):
            dp[0][j] = dp[0][j-1] and s2[j-1] == s3[j-1]
        for i in range(1, r+1):
            for j in range(1, c+1):
                dp[i][j] = (dp[i-1][j] and s1[i-1] == s3[i+j-1]) or\
                           (dp[i][j-1] and s2[j-1] == s3[i+j-1])

        return dp[-1][-1]
        # print(dp[-1][-1])

solutions.append(("O(m*n)", Solution().isInterleave))


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        l1, l2, l3 = len(s1)+1, len(s2)+1, len(s3)+1
        if l1 + l2 != l3+1: return False

        pre = [True for _ in range(l2)]

        for j in range(1, l2):
            pre[j] = pre[j-1] and s2[j-1] == s3[j-1]

        for i in range(1, l1):
            cur = [pre[0] and s1[i-1] == s3[i-1]] * l2
            for j in range(1, l2):
                cur[j] = (cur[j-1] and s2[j-1] == s3[i+j-1]) or\
                         (pre[j] and s1[i-1] == s3[i+j-1])
            pre = cur[:]

        return pre[-1]
        # print(pre[-1])


solutions.append(("O(2*n)", Solution().isInterleave))


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        r, c, l = len(s1), len(s2), len(s3)
        if r + c != l: return False

        dp = [True for _ in range(c+1)]

        for j in range(1, c+1):
            dp[j] = dp[j-1] and s2[j-1] == s3[j-1]

        for i in range(1, r+1):
            dp[0] = dp[0] and s1[i-1] == s3[i-1]
            for j in range(1, c+1):
                dp[j] = (dp[j] and s1[i-1] == s3[i+j-1]) or\
                        (dp[j-1] and s2[j-1] == s3[i+j-1])

        return dp[-1]
        # print(dp[-1])


solutions.append(("O(n)", Solution().isInterleave))


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        r, c, l = len(s1), len(s2), len(s3)
        if r + c != l: return False

        stack, visited = [(0, 0)], set((0, 0))

        while stack:
            x, y = stack.pop()
            if x + y == l:
                return True
                # print(True)
                # return
            if x+1 <= r and s1[x] == s3[x+y] and (x+1, y) not in visited:
                stack.append((x+1, y))
                visited.add((x+1, y))
            if y+1 <= c and s2[y] == s3[x+y] and (x, y+1) not in visited:
                stack.append((x, y+1))
                visited.add((x, y+1))

        return False
        # print(False)

solutions.append(("DFS", Solution().isInterleave))


class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        r, c, l = len(s1), len(s2), len(s3)
        if r + c != l: return False

        queue, visited = [(0, 0)], set((0, 0))

        while queue:
            x, y = queue.pop(0)
            # Notice pop(0) here ver pop() in stack solution
            if x + y == l:
                return True
                # print(True)
                # return
            if x+1 <= r and s1[x] == s3[x+y] and (x+1, y) not in visited:
                queue.append((x+1, y))
                visited.add((x+1, y))
            if y+1 <= c and s2[y] == s3[x+y] and (x, y+1) not in visited:
                queue.append((x, y+1))
                visited.add((x, y+1))

        return False
        # print(False)

solutions.append(("BFS", Solution().isInterleave))


for (s1, s2, s3, number) in ("hot", "dog", "hotdog", 10**6),\
                            ("aabccefghijk", "dbbcalmnopqr", "aadbbcbcacefghilmnopjkqr", 10),\
                            ("hot", "dog", "hotdog", 10):

    text = "\ns3={}"
    print(text.format(s3))
    for name, func in solutions:
        t = timeit(partial(func, s1, s2, s3), number=number) / number
        print("  %15s:  %8f seconds" % (name, t))


# test = Solution()
# test.isInterleave("aabcc", "dbbca", "aadbbcbcac") # True

# test = Solution()
# test.isInterleave("aabcc", "dbbca", "aadbbbaccc") # False

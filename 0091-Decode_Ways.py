from __future__ import annotations
from timeit import timeit
from functools import partial

"""
s=226
                    DP:  0.000002 seconds
      Short recurisive:  0.000001 seconds
           Memoization:  0.000000 seconds

s=232262222623
                    DP:  0.000010 seconds
      Short recurisive:  0.000005 seconds
           Memoization:  0.000002 seconds

s=226
                    DP:  0.000004 seconds
      Short recurisive:  0.000003 seconds
           Memoization:  0.000000 seconds
"""

solutions = []

class Solution:
    def numDecodings(self, s: str) -> int:
        if not s: return 0

        # dp[i] = the number of ways to parse the string s[1:i+1]
        dp = [0 for _ in range(len(s)+1)]
        dp[0] = 1 # set base case to make dp[2] valid
        dp[1] = 0 if s[0] == "0" else 1

        for i in range(2,len(s)+1):
            if 0 < int(s[i-1:i]):
                dp[i] += dp[i-1]
            if 10 <= int(s[i-2:i]) <= 26:
                dp[i] += dp[i-2]
        # print(dp)

        return dp[-1] # dp[len(s)]

solutions.append(("DP", Solution().numDecodings))


class Solution:
    def numDecodings(self, s: str) -> int:
        """
        preDecodes: previous number of ways to decode
        curDecodes: current number of ways to decode
        curDigit: current digit in s
        preDigit: previous digit in s
        """
        preDecodes = 0
        curDecodes = int(s > '')
        # int(s > ''): return 0 if empty string else 1
        preDigit = ''

        for curDigit in s:
            preDecodes, curDecodes, preDigit\
            = curDecodes,\
              (curDigit > '0')*curDecodes +\
              (10 <= int(preDigit+curDigit) <= 26)*preDecodes,\
              curDigit
              # curDigit > '0': return 0 if '0' else 1

            """
            Please note the following style leads to the different result
            in this case.
            preDecodes =
            curDecodes =
            preDigit =
            """

        return curDecodes
        # print(curDecodes)

solutions.append(("Short recurisive", Solution().numDecodings))


def memoize(f):
    memo = {}

    def wrapper(*args):
        if args not in memo:
            memo[args] = f(*args)
        return memo[args]

    return wrapper

class Solution:
    @memoize
    def numDecodings(self, s: str) -> int:
        if len(s) == 0:
            return 1
        elif len(s) == 1:
            if s[0] == '0':
                return 0
            else:
                return 1

        if int(s[-1]) > 0:
            if 10 <= int(s[-2:]) <= 26:
                return self.numDecodings(s[:-1]) + self.numDecodings(s[:-2])
            else:
                return self.numDecodings(s[:-1])
        elif 10 <= int(s[-2:]) <= 26:
            return self.numDecodings(s[:-2])
        else:
            return 0

solutions.append(("Memoization", Solution().numDecodings))


for (strings, number) in ("226", 10**6), ("232262222623", 10), ("226", 10):
    text = "\ns={}"
    print(text.format(strings))
    for name, func in solutions:
        t = timeit(partial(func, strings), number=number) / number
        print("  %20s:  %8f seconds" % (name, t))


# test = Solution()
# test.numDecodings("12") # 2

# test = Solution()
# test.numDecodings("226") # 3

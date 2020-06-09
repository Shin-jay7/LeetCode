from __future__ import annotations


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        n = len(s)
        dp = [True] + [False] * n

        for i in range(1, n+1):
            for word in wordDict:
                if s[:i].endswith(word):
                    dp[i] |= dp[i-len(word)]
                    # |= assures not to overwrite True
                    # think about the case below
                    # leetcode, [leet, code, ode]

        return dp[-1]
        # print(dp[-1])


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        dp = [True]

        for i in range(1, len(s)+1):
            dp += any(dp[j] and s[j:i]\
                  in wordDict for j in range(i)),

        """
        The comma actually changes the assignment value to be
        a tuple (iterable) and therefore extends the array.
        ---
        It seems quite a lot faster than even append
        >>> from timeit import timeit
        >>> timeit('x.append(1)', 'x = []', number=10000000)
        1.9880003412529277
        >>> timeit('x += 1,',     'x = []', number=10000000)
        1.2676891852971721
        >>> timeit('x += [1]',    'x = []', number=10000000)
        3.361207239950204
        """
        return dp[-1]
        # print(dp[-1])


test = Solution()
test.wordBreak("leetcode", ["leet", "code"]) # True

test = Solution()
test.wordBreak("applepenapple", ["apple", "pen"]) # True

test = Solution()
test.wordBreak("catsandog", ["cats", "dog", "sand", "and", "cat"]) # False

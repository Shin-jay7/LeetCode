from __future__ import annotations


class Solution:
    def nearestPalindromic(self, n: str) -> str:
        length = len(n)
        candidates = set((str(10**length+1), str(10**(length-1)-1)))
        prefix = int(n[:(length+1)//2])
        for pre in map(str, (prefix-1, prefix, prefix+1)):
            candidates.add(pre + [pre, pre[:-1]][length & 1][::-1])
        candidates.discard(n)
        return min(candidates, key=lambda x: (abs(int(x) - int(n)), int(x)))


test = Solution()
test.nearestPalindromic("123")  # "121"

test = Solution()
test.nearestPalindromic("1234")  # "1221"

test = Solution()
test.nearestPalindromic("1")  # "0"

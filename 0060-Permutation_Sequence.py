from __future__ import annotations
import math


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        """
        say n = 4, k = 14
        [1,2,3,4]
        1 + (permutations of 2,3,4 -> 6 perms)
        2 + (permutations of 2,3,4 -> 6 perms)
        3 + (permutations of 2,3,4 -> 6 perms)  <- here!: index = (k-1) // 6
        4 + (permutations of 2,3,4 -> 6 perms)
        """
        ans = ""
        nums = [str(_) for _ in range(1,n+1)]
        fact = math.factorial(n)
        k -= 1

        while nums:
            fact //= len(nums)
            idx, k = divmod(k, fact)
            ans += nums.pop(idx)

        return ans
        # print(ans)


test = Solution()
test.getPermutation(3,3) # "213"

test = Solution()
test.getPermutation(4,14) # "3142"

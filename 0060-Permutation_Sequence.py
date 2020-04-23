from __future__ import annotations


class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        ans = [[]]

        for num in range(1,n+1):
            perm = []
            for l in ans:
                for i in range(len(l)+1):
                    perm.append(l[:i]+[num]+l[i:])
            ans = perm

        return "".join(map(str, sorted(ans)[k-1]))
        # print("".join(map(str, sorted(ans)[k-1])))


test = Solution()
test.getPermutation(3,3) # "213"

test = Solution()
test.getPermutation(4,9) # "2314"

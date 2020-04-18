from __future__ import annotations


class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        for n in nums:
            # print("** first loop begins")
            # print("n: "+str(n))
            perm = []
            for l in ans:
                # print("** second loop begins **")
                # print("l: "+str(l))
                # print("(l+[n]).index(n)+1: "+str((l+[n]).index(n)+1))
                #               ↓ this trick skips duplicate case
                for i in range((l+[n]).index(n)+1):
                    # print("** third loop begins")
                    # print("i: "+str(i))
                    # print("l[:i]+[n]+l[i:]: "+str(l[:i]+[n]+l[i:]))
                    perm.append(l[:i]+[n]+l[i:])
                    # print("perm: "+str(perm))
            #         print("** third loop ends**")
            #     print("** second loop ends**")
            # print("** first loop ends**")
            ans = perm
            # print("ans: "+str(ans))

        # print(ans)
        return ans


test = Solution()
test.permuteUnique([1,1,2,3])

# test = Solution()
# test.permuteUnique([1,1,2])
"""
[
  [1,1,2],
  [1,2,1],
  [2,1,1]
]
"""

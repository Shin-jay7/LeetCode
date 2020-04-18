from __future__ import annotations

"""
either the new element does not exist in rest (in this case just insert it
everywhere like before) or we only insert up to the first occurrence
rest.index(head), because any other slot after the first occurrence can be
thought as the duplicate of the first occurrence as the inserted element
and the slot being the existing one.
"""

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]
        for n in nums:
            # print("** first loop begins")
            # print("n: "+str(n))
            perms = []
            for l in ans:
                # print("** second loop begins")
                # print("l: "+str(l))
                # print("(l+[n]).index(n)+1: "+str((l+[n]).index(n)+1))
                for i in range((l+[n]).index(n)+1):
                    # print("** third loop begins")
                    # print("i: "+str(i))
                    # print("l[:i]+[n]+l[i:]: "+str(l[:i]+[n]+l[i:]))
                    perms.append(l[:i]+[n]+l[i:])
            #         print("** third loop ends**")
            #     print("** second loop ends**")
            # print("** first loop ends**")
            ans = perms
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

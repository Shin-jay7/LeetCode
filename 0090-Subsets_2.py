from __future__ import annotations
from itertools import combinations
from timeit import timeit
from functools import partial
from collections import Counter

"""
nums=[1, 2, 2]
                    Recursive:  0.000002 seconds
            Another recursive:  0.000002 seconds
                          DFS:  0.000003 seconds
               DFS with yield:  0.000004 seconds
  Lexicographic/Binary Sorted:  0.000007 seconds
                      Library:  0.000002 seconds

nums=[1, 2, 2, 3, 3, 4, 4, 5]
                    Recursive:  0.000017 seconds
            Another recursive:  0.000017 seconds
                          DFS:  0.000054 seconds
               DFS with yield:  0.000069 seconds
  Lexicographic/Binary Sorted:  0.000420 seconds
                      Library:  0.000030 seconds

nums=[1, 2, 2]
                    Recursive:  0.000002 seconds
            Another recursive:  0.000004 seconds
                          DFS:  0.000007 seconds
               DFS with yield:  0.000007 seconds
  Lexicographic/Binary Sorted:  0.000011 seconds
                      Library:  0.000007 seconds
"""

solutions = []

class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans , res = [[]], []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i-1]:
                res = [item + [nums[i]] for item in res]
            else:
                res = [item + [nums[i]] for item in ans]
            ans += res

        return ans
        # print(ans)

solutions.append(("Recursive", Solution().subsetsWithDup))


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        ans, pos = [[]], {}
        for n in nums:
            idx, l = pos.get(n, 0), len(ans)
            ans += [r + [n] for r in ans[idx:]]
            pos[n] = l

        return ans
        # print(ans)

solutions.append(("Another recursive", Solution().subsetsWithDup))


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        ans = []
        nums.sort()
        self.dfs(nums, 0, [], ans)

        return ans
        # print(ans)

    def dfs(self, nums, idx, path, ans):
        ans.append(path)
        for i in range(idx, len(nums)):
            if i > idx and nums[i] == nums[i-1]:
                continue
            self.dfs(nums, i+1, path+[nums[i]], ans)

solutions.append(("DFS", Solution().subsetsWithDup))


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        def dfs(acc, pos):
            yield acc
            for i in range(pos, len(nums)):
                if i > pos and nums[i] == nums[i-1]:
                    continue
                yield from dfs(acc+[nums[i]], i+1)

        return list(dfs([], 0))
        # print(list(dfs([], 0)))

solutions.append(("DFS with yield", Solution().subsetsWithDup))


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """
        Generate all possible binary bitmasks of length n.
        Map a subset to each bitmask: 1 on the ith position in bitmask
        means the presence of nums[i] in the subset,
        and 0 means its absence.
        """
        nums.sort()
        n = len(nums)
        ans, res = [], []

        for i in range(2**n, 2**(n+1)):
            # generate bitmask, from 0..00 to 1..11
            bitmask = bin(i)[3:]
            res = [nums[j] for j in range(n) if bitmask[j] == '1']
            if res not in ans:
                ans.append(res)

        return ans
        # print(ans)

solutions.append(("Lexicographic/Binary Sorted", Solution().subsetsWithDup))


class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """
        sum(iterable, start):
        The `sum()` function adds `start` and items of the given `iterable`
        from left to right

        But this case, [] in `sum(ans,[])` seems to work for changing from
        lists in lists in list to lists in list???????
        """
        nums.sort()
        ans = []
        for i in range(len(nums)+1):
            ans.append(list(combinations(nums, i)))

        return list(set(sum(ans,[])))
        # print(list(set(sum(ans,[]))))

solutions.append(("Library", Solution().subsetsWithDup))


for (nums, number) in ([1,2,2], 10**6),\
                      ([1,2,2,3,3,4,4,5], 10),\
                      ([1,2,2], 10):
    text = "\nnums={}"
    print(text.format(nums))
    for name, func in solutions:
        t = timeit(partial(func, nums), number=number) / number
        print("  %27s:  %8f seconds" % (name, t))


# test = Solution()
# test.subsetsWithDup([1,2,2])
"""
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]
"""

# test = Solution()
# test.subsetsWithDup([1,1,2,2])
"""
[[],[1],[1,1],[1,1,2],[1,1,2,2],[1,2],[1,2,2],[2],[2,2]]
"""

# test = Solution()
# test.subsetsWithDup([4,4,4,1,4])
"""
[[],[1],[1,4],[1,4,4],[1,4,4,4],[1,4,4,4,4],[4],[4,4],[4,4,4],[4,4,4,4]]
"""


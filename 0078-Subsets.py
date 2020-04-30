from __future__ import annotations
from itertools import combinations
from timeit import timeit
from functools import partial


solutions = []

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        ans = [[]]

        for num in nums:
            ans += [i+[num] for i in ans]

        return ans
        # print(ans)

solutions.append(("Recursive", Solution().subsets))


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def backtrack(first=0, curr=[]):
            if len(curr) == k:
                ans.append(curr[:])

            for i in range(first, n):
                curr.append(nums[i])
                backtrack(i+1, curr)
                curr.pop()

        ans = []
        n = len(nums)

        for k in range(n+1):
            backtrack()

        return ans
        # print(ans)

solutions.append(("Backtracking", Solution().subsets))


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        """
        Generate all possible binary bitmasks of length n.
        Map a subset to each bitmask: 1 on the ith position in bitmask
        means the presence of nums[i] in the subset,
        and 0 means its absence.
        """
        n =len(nums)
        ans = []

        for i in range(2**n, 2**(n+1)):
            # generate bitmask, from 0..00 to 1..11
            bitmask = bin(i)[3:]
            ans.append([nums[j] for j in range(n) if bitmask[j] == '1'])

        return ans
        # print(ans)

solutions.append(("Lexicographic/Binary Sorted", Solution().subsets))


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        return sum([list(combinations(nums, i)) for i in range(len(nums)+1)], [])
        # print(sum([list(combinations(nums, i)) for i in range(len(nums)+1)], []))


solutions.append(("Library", Solution().subsets))


"""
nums=[1, 2, 3]
  Recursive:  0.00000129 seconds
  Backtracking:  0.00001584 seconds
  Lexicographic/Binary Sorted:  0.00000639 seconds
  Library:  0.00000188 seconds

nums=[0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
  Recursive:  0.00010853 seconds
  Backtracking:  0.00460754 seconds
  Lexicographic/Binary Sorted:  0.00131374 seconds
  Library:  0.00005847 seconds

nums=[1, 2, 3]
  Recursive:  0.00000168 seconds
  Backtracking:  0.00001693 seconds
  Lexicographic/Binary Sorted:  0.00000718 seconds
  Library:  0.00000245 seconds
"""

for (nums, number) in ([1,2,3], 10**6),\
                      ([i for i in range(10)], 10**1),\
                      ([1,2,3], 10):
    text = "\nnums={}"
    print(text.format(nums))
    for name, func in solutions:
        t = timeit(partial(func, nums), number=number) / number
        print("  %7s:  %.8f seconds" % (name, t))


# test = Solution()
# test.subsets([1,2,3])
"""
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]
"""

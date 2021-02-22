from __future__ import annotations


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        ans = []
        self.dfs(list(range(1, 10)), k, n, [], ans)
        return ans

    def dfs(self, nums, k, n, path, ans):
        if k < 0 or n < 0:
            return
        if k == 0 and n == 0:
            ans.append(path)
        for i in range(len(nums)):
            if nums[i] + (k-1) > n:
                break
            self.dfs(nums[i+1:], k-1, n-nums[i], path+[nums[i]], ans)


from itertools import combinations
class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        return [c for c in combinations(range(1, 10), k) if sum(c) == n]


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def combs(k, n, cap):
            if not k:
                return [[]] * (not n)
            return [comb + [last]
                    for last in range(1, cap)
                    for comb in combs(k-1, n-last, last)]
        return combs(k, n, 10)


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        combs = [[]]
        for _ in range(k):
            combs = [[first] + combs
                     for comb in combs
                     for first in range(1, comb[0] if comb else 10)]

        return [c for c in combs if sum(c) == n]


class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        return [c for c in 
                reduce(lambda combs, _: [[first] + comb
                                         for comb in combs
                                         for first in range(1, comb[0] if comb else 10)],
                                         range(k), [[]]) if sum(c) == n]

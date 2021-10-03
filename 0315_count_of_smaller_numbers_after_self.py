from __future__ import annotations
from typing import List


class Solution:
    # https://leetcode.com/problems/count-of-smaller-numbers-after-self/discuss/76584/Mergesort-solution/735423
    def countSmaller(self, nums: List[int]) -> List[int]:
        def sort(enum):
            len_e = len(enum)
            half = len_e // 2
            if half:
                left, right = sort(enum[:half]), sort(enum[half:])
                for i in range(len_e)[::-1]:
                    if not right or left and left[-1][1] > right[-1][1]:
                        smallers[left[-1][0]].append(len(right))
                        enum[i] = left.pop()
                    else:
                        enum[i] = right.pop()
            return enum

        smallers = [0] * len(nums)
        sort(list(enumerate(nums)))
        return smallers


class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        rank = {val: i+1 for i, val in enumerate(sorted(nums))}
        length = len(nums)
        bi_tree = [0]*(length+1)
        smallers = []

        def update(i):
            while i <= length:
                bi_tree[i] += 1
                i += i & -i

        def getSum(i):
            ans = 0
            while i:
                ans += bi_tree[i]
                i -= i & -i
            return ans

        for num in reversed(nums):
            smallers.append(getSum(rank[num]-1)),
            update(rank[num])

        return smallers[::-1]

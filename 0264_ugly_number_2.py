from __future__ import annotations


class Solution:
    def nthUglyNumber(self, n: int) -> int:
        factors, indexes, nums = [2, 3, 5], [0, 0, 0], [1]

        for _ in range(n-1):
            candidates = [factors[i] * nums[indexes[i]] for i in range(3)]
            num = min(candidates)
            nums.append(num)
            indexes = [indexes[i] + (candidates[i] == num) for i in range(3)]

        return nums[-1]

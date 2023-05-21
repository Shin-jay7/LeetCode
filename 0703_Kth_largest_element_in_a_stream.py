from __future__ import annotations
from heapq import heapify, heappush, heappop, nlargest
from bisect import insort


# Time limit exceeded
class KthLargest:
    def __init__(self, k: int, nums: list[int]):
        self.heap = nums
        self.k = k
        heapify(self.heap)

    def add(self, val: int) -> int:
        heappush(self.heap, val)
        return nlargest(self.k, self.heap)


class KthLargest:
    def __init__(self, k: int, nums: list[int]):
        self.heap = []
        self.k = k
        for num in nums:
            self.add(num)

    def add(self, val: int) -> int:
        heappush(self.heap, val)
        if len(self.heap) > self.k:
            heappop(self.heap)
        return self.heap[0]


class KthLargest:
    def __init__(self, k: int, nums: list[int]):
        self.k = k
        self.nums = sorted(nums)

    def add(self, val: int) -> int:
        insort(self.nums, val)
        return self.nums[-self.k]

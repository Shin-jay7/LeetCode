from __future__ import annotations
from heapq import heappush, heappushpop


class MedianFinder:
    def __init__(self) -> None:
        self.heaps = [], []

    def addNum(self, num: int) -> None:
        small, large = self.heaps
        if len(small) == len(large):
            heappush(large, -heappushpop(small, -num))
        else:
            heappush(small, -heappushpop(large, num))

    def findMedian(self) -> float:
        small, large = self.heaps
        if len(small) == len(large):
            return (large[0] - small[0]) / 2
        else:
            return float(large[0])

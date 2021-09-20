from __future__ import annotations


class MedianFinder:
    def __init__(self) -> None:
        self.arr = []

    def addNum(self, num: int) -> None:
        self.arr.append(num)

    def findMedian(self) -> float:
        arr = sorted(self.arr)
        length = len(arr)
        if length % 2:
            return arr[length // 2] / 1.0
        else:
            return (arr[length // 2 - 1] + arr[length // 2])/2

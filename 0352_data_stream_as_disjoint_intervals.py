from __future__ import annotations
from typing import List
from heapq import heappop, heappush


class SummaryRanges:
    def __init__(self):
        self.intvals = []
        self.seen = set()

    def addNum(self, val: int) -> None:
        if val not in self.seen:
            self.seen.add(val)
            heappush(self.intvals, [val, val])
            # print(self.intvals)

    def getIntervals(self) -> List[List[int]]:
        new_intvals = []
        while self.intvals:
            # The heappop() function removes and returns the smallest element from the heap.
            next_intval = heappop(self.intvals)
            if new_intvals and next_intval[0] <= new_intvals[-1][1]+1:
                new_intvals[-1][1] = max(new_intvals[-1][1], next_intval[1])
            else:
                new_intvals.append(next_intval)

        self.intvals = new_intvals
        return self.intvals
        # print(self.intvals)


test = SummaryRanges()
test.addNum(1)
test.getIntervals() # [[1, 1]]
test.addNum(3)
test.getIntervals() # [[1, 1], [3, 3]]
test.addNum(7)
test.getIntervals() # [[1, 1], [3, 3], [7, 7]]
test.addNum(2)
test.getIntervals() #  [[1, 3], [7, 7]]
test.addNum(6)
test.getIntervals() # [[1, 3], [6, 7]]

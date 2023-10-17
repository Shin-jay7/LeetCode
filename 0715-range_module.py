from __future__ import annotations
from bisect import bisect_left as bl, bisect_right as br


class RangeModule:
    def __init__(self):
        self.track = []

    def addRange(self, left: int, right: int) -> None:
        start, end = bl(self.track, left), br(self.track, right)
        # print(f'start: {start}, end: {end}')
        subtrack = []
        if start % 2 == 0:
            subtrack.append(left)
        if end % 2 == 0:
            subtrack.append(right)
        self.track[start:end] = subtrack
        # print(f'track: {self.track}')
        # print('---')

    def removeRange(self, left: int, right: int) -> None:
        start, end = bl(self.track, left), br(self.track, right)
        # print(f'start: {start}, end: {end}')
        subtrack = []
        if start % 2 == 1:
            subtrack.append(left)
        if end % 2 == 1:
            subtrack.append(right)
        self.track[start:end] = subtrack
        # print(f'track: {self.track}')
        # print('---')
    
    def queryRange(self, left: int, right: int) -> bool:
        start, end = br(self.track, left), bl(self.track, right)
        # print(f'left: {left}, right: {right}')
        # print(f'start: {start}, end: {end}')
        print(start == end and start % 2 == 1)
        # print('---')
        return start == end and start % 2 == 1
        

test = RangeModule()
test.addRange(10, 20)
test.removeRange(14, 16)
test.queryRange(10, 14) # True
test.queryRange(13, 15) # False
test.queryRange(16, 17) # True

test = RangeModule()
test.addRange(10, 20)
test.removeRange(15, 20)
test.queryRange(10, 14) # True
test.queryRange(13, 15) # True
test.queryRange(16, 17) # False

test = RangeModule()
test.addRange(10, 20)
test.addRange(15, 25)

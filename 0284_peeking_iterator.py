from __future__ import annotations


class PeekingIterator:
    def __init__(self, iterator):
        self.iter = iterator
        self.temp = self.iter.next() if self.iter.hasNext() else None

    def peek(self):
        return self.temp
    
    def next(self):
        ans = self.temp
        self.temp = self.iter.next() if self.iter.hasNext() else None
        return ans

    def hasNext(self) -> bool:
        return self.temp is not None
   
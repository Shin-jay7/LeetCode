from __future__ import annotations
from collections import deque


"""
This is the interface that allows for creating nested lists.
You should not implement it, or speculate about its implementation
"""
class NestedInteger:
   def isInteger(self) -> bool:
       """
       @return True if this NestedInteger holds a single integer, rather than a nested list.
       """

   def getInteger(self) -> int:
       """
       @return the single integer that this NestedInteger holds, if it holds a single integer
       Return None if this NestedInteger holds a nested list
       """

   def getList(self) -> [NestedInteger]:
       """
       @return the nested list that this NestedInteger holds, if it holds a nested list
       Return None if this NestedInteger holds a single integer
       """


class NestedIterator:
    def __init__(self, nestedList: [NestedInteger]):
        self.deq = deque(nestedList)

    def FixDeque(self):
        last = self.deq.popleft()
        for e in last.getList()[::-1]:
            self.deq.appendleft(e)
        
    def next(self) -> int:
        first = self.deq[0]
        if first.isInteger():
            self.deq.popleft()
            return first.getInteger()
        else:
            self.FixDeque()
            return self.next()

    def hasNext(self) -> bool:
        while self.deq and not self.deq[0].isInteger():
            self.FixDeque()
        return self.deq


class NestedIterator():
    def __init__(self, nestedList: [NestedInteger]):
        self.stack = [[nestedList, 0]]
        
    def next(self) -> int:
        self.hasNext()
        nestedList, i = self.stack[-1]
        self.stack[-1][1] += 1
        return nestedList[i].getInteger()

    def hasNext(self) -> bool:
        s = self.stack
        while s:
            nestedList, i = s[-1]
            if i == len(nestedList):
                s.pop()
            else:
                x = nestedList[i]
                if x.isInteger():
                    return True
                s[-1][1] += 1
                s.append([x.getList(), 0])
        return False


class NestedIterator():
    def __init__(self, nestedList: [NestedInteger]):
        self.peek = None
        def gen(nestedList):
            for x in nestedList:
                if x.isInteger():
                    yield x.getInteger()
                else:
                    for y in gen(x.getList()):
                        yield y
        self.gen = gen(nestedList)
        
    def next(self) -> int:
        if self.peek is None:
            return next(self.gen)
        else:
            tmp = self.peek
            self.peek = None
            return tmp
    
    def hasNext(self) -> bool:
        if self.peek is None:
            try:
                self.peek = next(self.gen)
                return True
            except StopIteration:
                return False
        else:
            return True

from __future__ import annotations
from typing import List
from itertools import accumulate
from bisect import bisect_left
from random import randint, uniform


class Solution:
    def __init__(self, w: List[int]):
        self.w = list(accumulate(w))

    def pickIndex(self) -> int:
        return bisect_left(self.w, randint(1, self.w[-1]))


class Solution:
    def __init__(self, w: List[int]):
        for i in range(1, len(w)):
            w[i] += w[i-1]
        self.w = w

    def pickIndex(self) -> int:
        left, right = 0, len(self.w) - 1
        target = randint(1, self.w[-1])
        while left < right:
            mid = (left + right) // 2
            if target <= self.w[mid]:
                right = mid
            else:
                left = mid+1
        return left


# https://en.wikipedia.org/wiki/Alias_method
# https://www.keithschwarz.com/darts-dice-coins/
class Solution:
    def __init__(self, w):
        self.n, self.boxes = len(w), []
        # If you do not include the epsilon then it is possible for the while statement
        # to complete with zero big items even though there is a small item remaining. 
        # You may have a big item which, after adjustment, is mathematically equal to size
        # but numerically ever so slightly less, and your code will transfer it to small
        # if you do not have the epsilon there. Your following code as it is written would
        # not then append this remaining "small" item, which is really a practically full
        # box, to the list of boxes. The easy fix is just to append all items big and small
        # as full boxes once either big or small is found to be empty. This can only
        # introduce a negligible numerical error.
        # The reason you have to be careful is of course the finite numerical precision.
        # One way to save the precision, although it may not appeal to you because of the
        # large integers potentially involved, would be to multiply all integer weights by
        # the number of classes and work directly with these raw magnified integer weights.
        ep = 10e-5
        weights = [weight / sum(w) for weight in w]
        size = 1 / self.n
        big_weights = {i: x for i, x in enumerate(weights) if x >= size}
        small_weights = {i: x for i, x in enumerate(weights) if x < size}
        while big_weights and small_weights:
            i = next(iter(big_weights))
            j, w_j = small_weights.popitem()
            self.boxes.append([j, i, w_j])
            big_weights[i] -= (size - w_j)
            if big_weights[i] < size - ep:
                small_weights[i] = big_weights.pop(i)

        self.boxes.extend([key] for key in big_weights)

    def pickIndex(self):
        box_num = randint(0, self.n - 1)
        if len(self.boxes[box_num]) == 1:
            return self.boxes[box_num][0]

        return self.boxes[box_num][uniform(0, 1 / self.n) >= self.boxes[box_num][2]]

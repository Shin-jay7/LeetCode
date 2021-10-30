from __future__ import annotations
from random import choice


class RandomizedSet:
    def __init__(self):
        self.nums_dic = {}
        self.nums = []

    def insert(self, val: int) -> bool:
        # checking if item is in the
        # dictionary is on average O(1) where as
        # checking the list is on average O(n)
        if val in self.nums_dic:
            return False
        # len is equal to the index of the last item + 1,
        # which points to the index of a new element
        self.nums_dic[val] = len(self.nums)
        self.nums.append(val)

    def remove(self, val: int) -> bool:
        if val not in self.nums_dic:
            return False
        """
        move the last num in the list into the location of the nums we want to
        remove. this is a significantly more efficient operation than the
        obvious solution of removing the item and shifting the values of every
        item in the dicitionary to match their new position in the list
        """
        last_num_in_list = self.nums[-1]
        idx_of_num_to_remove = self.nums_dic[val]
        self.nums_dic[last_num_in_list] = idx_of_num_to_remove
        self.nums[idx_of_num_to_remove] = last_num_in_list
        self.nums[-1] = val
        self.nums.pop()
        self.nums_dic.pop(val)
        return True

    def getRandom(self) -> int:
        return choice(self.nums)


class RandomizedSet:
    def __init__(self):
        self.nums = []

    def insert(self, val: int) -> bool:
        if val not in self.nums:
            self.nums.append(val)
            return True
        return False

    def remove(self, val: int) -> bool:
        if val in self.nums:
            self.nums.remove(val)
            return True
        return False

    def getRandom(self) -> int:
        return choice(self.nums)

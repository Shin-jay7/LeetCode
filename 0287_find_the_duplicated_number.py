from __future__ import annotations
from typing import List


"""
the problem is to find the starting point of loop in singly-linked list,
which has a classical solution with two pointers: 
slow which moves one step at a time and fast, which moves two times at a time.
To find this place we need to do it in two iterations: first we wait until
fast pointer gains slow pointer and then we move slow pointer to the start
and run them with the same speed and wait until they concide.
"""
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        slow, fast = nums[0], nums[0]
        # print("Begin")
        # print(slow, fast)
        # print("First loop")
        while True:
            slow, fast = nums[slow], nums[nums[fast]]
            # print(slow, fast)
            if slow == fast:
                break

        slow = nums[0]
        # print("Prepare for the second loop")
        # print(slow, fast)
        # print("Second loop")
        while slow != fast:
            slow, fast = nums[slow], nums[fast]
            # print(slow, fast)

        return slow

# https://leetcode.com/problems/find-the-duplicate-number/discuss/704693/Python-2-solutions%3A-Linked-List-Cycle-O(n)-and-BS-O(n-log-n)-explained


test = Solution()
test.findDuplicate( [1,3,4,2,2]) # 2

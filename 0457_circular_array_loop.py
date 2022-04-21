from __future__ import annotations
from typing import List


class Solution:
    def circularArrayLoop(self, nums: List[int]) -> bool:
        # Store the mapping from each index to its next one to save computing every time
        indexes = {idx: (idx+num) % len(nums) for idx, num in enumerate(nums)}
        # Compute the path starting at each index in paths
        # Filter out 1 element cycles as part of defining the first path
        paths = {key: val for key, val in indexes.items() if key != val}

        while len(paths) > 0:
            if any(idx == next_idx for idx, next_idx in paths.items()):
                return True
            paths = {
                 idx: indexes[next_idx]
                 # Filter out an index in a given path if the direction changes
                 # or the next index is already filtered out 
                 for idx, next_idx in paths.items()
                 if nums[idx] * nums[next_idx] > 0 and next_idx in paths
                }

        return False

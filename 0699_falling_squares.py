from __future__ import annotations
from typing import List


class Solution:
    def fallingSquares(self, positions: List[List[int]]) -> List[int]:
        heights = [0] * len(positions)
        for i, (left, size) in enumerate(positions):
            right = left + size
            heights[i] += size
            for j in range(i+1, len(positions)):
                next_left, next_size = positions[j]
                next_right = next_left + next_size
                if next_left < right and next_right > left:
                    heights[j] = max(heights[j], heights[i])

        ans = []
        for height in heights:
            ans.append(max(height, ans[-1]) if ans else height)
        return ans

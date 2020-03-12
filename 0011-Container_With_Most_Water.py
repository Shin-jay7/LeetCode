from __future__ import annotations

class Solution:
    def maxArea(self, height: List[int]) -> int:
        max_, l, r = 0, 0, len(height)-1
        while l < r:
            max_ = max(max_, (r-l)*min(height[l],height[r]))
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1

        return max_


test = Solution()
test.maxArea([1,8,6,2,5,4,8,3,7]) # 49

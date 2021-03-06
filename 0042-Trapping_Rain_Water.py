from __future__ import annotations


class Solution:
    def trap(self, height: List[int]) -> int:
        if not height or len(height) < 2:
            return 0

        vol, l, r = 0, 0, len(height)-1
        l_max, r_max = height[l], height[r]

        while l < r:
            if height[l] < height[r]:
                if height[l] > l_max:
                    l_max = height[l]
                else:
                    vol += l_max - height[l]
                l += 1
            else:
                if height[r] > r_max:
                    r_max = height[r]
                else:
                    vol += r_max - height[r]
                r -= 1

        return vol


test = Solution()
test.trap([0,1,0,2,1,0,1,3,2,1,2,1]) # 6

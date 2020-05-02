from __future__ import annotations


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        length = len(heights)
        l, r, max_ = 0, 0, 0

        while l < length:
            if heights[l]:
                H = heights[l]
                while r < length:
                    if l > r:
                        r = l
                        continue
                    if not heights[r]:
                        break
                    H = min(H, heights[r])
                    W = (r-l) + 1
                    max_ = max(max_, H*W)
                    r += 1
            l += 1
            r = 0

        return max_
        # print(max_)


test = Solution()
test.largestRectangleArea([2,1,5,6,2,3]) # 10

test = Solution()
test.largestRectangleArea([1]) # 1

test = Solution()
test.largestRectangleArea([2,0,3]) # 3

test = Solution()
test.largestRectangleArea([0,9]) # 9

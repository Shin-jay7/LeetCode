from __future__ import annotations


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        n = len(heights)
        left, right = [1]*n, [1]*n
        """
        left[i] to indicate how many continuous bars to the left (including
        the bar at index i) are equal or higher than bar[i], right[i] is that
        to the right of bar[i], so the the square of the max rectangle
        containing bar[i] is simply height[i] * (left[i] + right[i] - 1)
        """

        # calculate left
        for i in range(1,n):
            j = i-1
            """
            The while loop in the for loop jumps forward or backward
            by the steps already calculated.
            """
            while j >= 0 and heights[j] >= heights[i]:
                j -= left[j]
            left[i] = i-j

        # calculate right
        for i in range(n-2,-1,-1):
            j = i+1
            while j < n and heights[i] <= heights[j]:
                j += right[j]
            right[i] = j-i

        ans = 0
        for i in range(n):
            ans = max(ans, heights[i]*(left[i]+right[i]-1))

        return ans
        # print(ans)


test = Solution()
test.largestRectangleArea([2,1,5,6,2,3]) # 10

test = Solution()
test.largestRectangleArea([1]) # 1

test = Solution()
test.largestRectangleArea([2,0,3]) # 3

test = Solution()
test.largestRectangleArea([0,9]) # 9

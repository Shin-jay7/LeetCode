from __future__ import annotations


class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        """
        For any bar x, if it's in a rectangle of which the height is also
        the height of x, we know that every bar in the rectangle must be
        no shorter than x. Then the issue is to find the left and right
        boundary where the bars are shorter than x. According to the code,
        when a bar is popped out from the stack, we know it must be higher
        than the bar at position i, so bar[i] must be the right boundary
        (exclusive) of the rectangle, and the previous bar in the stack is
        the first one that is shorter than the popped one so it must be the
        left boundary (also exclusive). Then we find the rectangle.
        """
        heights.append(0)
        """
        Because for some heights there is no any other lower height
        at its right side. Adding a 0 at the last makes all rectangles
        able to find their right-side boundary.
        We add a zero at the end because we want to always ensure a condition
        in which the current considered height is less than the height's stored
        in the stack.
        """
        stack = [-1]
        """
        We instantiate the stack with -1 as a reference the 0 that we added to
        height. The zero serves a couple functions:
        • It always adds the first height to the stack so it's not empty
        • In the case that the heights are in ascending order, it creates
          an ending point that breaks this, allowing us to calculate the areas
        In cases when stack has only one element i.e. -1 then stack[-1] = -1
        and so heights[stack[-1]] = heights[-1] = 0 because we appended 0 to
        heights and 0 is smaller than all other heights, so popping will stop
        there and -1 will never be popped out of the stack and so this works as
        a stopping criterion (instead of doing something like 'if stack').
        """
        ans = 0

        for i in range(len(heights)):
            while heights[i] < heights[stack[-1]]:
                """
                the while condition is true when we see a height that's smaller
                than height stored at the top of the stack.
                """
                H = heights[stack.pop()]
                """
                the current h is guaranteed to the be the limiting height
                (remember the stack is ascending so everything to it's right
                 was >= h)
                """
                W = i-stack[-1]-1
                """
                key thing to remember here is stack is always ascending,
                so i-1 represents the right boundary of the considered rectangle
                and stack[-1] represents the left boundary. So subtracting them
                gets you the width!
                """
                ans = max(ans, H*W)
            stack.append(i)

        heights.pop()
        """
        this line is to recover the original state of the input, since python
        list is passed by reference instead of shadow copy. It is not gonna
        give you wrong result for this problem. However in real world
        development, think about your colleague created a list contains some
        values that he will need in the future, you added a sentinel value to
        make your life easier, if you don't clean it up afterward, your
        colleague's code is very likely to crash. This is a good programming
        habit, it added one more "redundant" line, but it also make everybody's
        life easier.
        """

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

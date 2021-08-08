from __future__ import annotations


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        ranges, stack = [], []

        for n in (nums):
            if n-1 not in stack:
                stack = []
                ranges.append(stack)
            stack[1:] = [n]
            # print("stack:" + str(stack))
            # print("ranges:" + str(ranges))
            # ---
            # stack:[0]
            # ranges:[[0]]
            # stack:[0, 1]
            # ranges:[[0, 1]]
            # stack:[0, 2]
            # ranges:[[0, 2]]
            # stack:[4]
            # ranges:[[0, 2], [4]]
            # stack:[4, 5]
            # ranges:[[0, 2], [4, 5]]
            # stack:[7]
            # ranges:[[0, 2], [4, 5], [7]]
            # ---

        return ['->'.join(map(str, r)) for r in ranges]
        # print(['->'.join(map(str, r)) for r in ranges])


test = Solution()
test.summaryRanges([0,1,2,4,5,7]) # ["0->2","4->5","7"]


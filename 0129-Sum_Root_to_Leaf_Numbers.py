from __future__ import annotations
from timeit import timeit
from functools import partial


solutions = []

class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""
testCase=1
       stack:  0.000001 seconds
       queue:  0.000001 seconds
   recursive:  0.000001 seconds

testCase=2
       stack:  0.000005 seconds
       queue:  0.000005 seconds
   recursive:  0.000008 seconds

testCase=3
       stack:  0.000002 seconds
       queue:  0.000001 seconds
   recursive:  0.000004 seconds
"""


class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root: return 0

        stack, ans = [(root, root.val)], 0

        while stack:
            node, value = stack.pop()
            if node:
                if not node.left and not node.right:
                    ans += value
                if node.right:
                    stack.append((node.right, value*10+node.right.val))
                if node.left:
                    stack.append((node.left, value*10+node.left.val))

        return ans
        # print(ans)


solutions.append(("stack", Solution().sumNumbers))


from collections import deque
class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        if not root: return 0

        queue, ans = deque([(root, root.val)]), 0

        while queue:
            node, value = queue.popleft()
            if node:
                if not node.left and not node.right:
                    ans += value
                if node.left:
                    queue.append((node.left, value*10+node.left.val))
                if node.right:
                    queue.append((node.right, value*10+node.right.val))

        return ans
        # print(ans)

solutions.append(("queue", Solution().sumNumbers))


class Solution:
    def sumNumbers(self, root: TreeNode) -> int:
        self.ans = 0
        self.dfs(root, 0)

        # print(self.ans)
        return self.ans

    def dfs(self, node, value):
        if node:
            val, left, right = node.val, node.left, node.right
            self.dfs(left, value*10+val)
            self.dfs(right, value*10+val)
            if not left and not right:
                self.ans += value*10+val

solutions.append(("recursive", Solution().sumNumbers))


for (root, testCase, number) in (TreeNode(1, TreeNode(2), TreeNode(3)), 1, 10**7),\
                                (TreeNode(4, TreeNode(9, TreeNode(5), TreeNode(1, TreeNode(6, None, TreeNode(7)))), TreeNode(0, TreeNode(2, None, TreeNode(8)), TreeNode(3))), 2, 10),\
                                (TreeNode(1, TreeNode(2), TreeNode(3)), 3, 10):
    text = "\ntestCase={}"
    print(text.format(testCase))
    for name, func in solutions:
        t = timeit(partial(func, root), number=number) / number
        print("  %10s:  %8f seconds" % (name, t))


# test = Solution()
# test.sumNumbers(TreeNode(1, TreeNode(2), TreeNode(3)))
# """
# The root-to-leaf path 1->2 represents the number 12.
# The root-to-leaf path 1->3 represents the number 13.
# Therefore, sum = 12 + 13 = 25.
# """

# test = Solution()
# test.sumNumbers(TreeNode(4, TreeNode(9, TreeNode(5), TreeNode(1)), TreeNode(0)))
# """
# The root-to-leaf path 4->9->5 represents the number 495.
# The root-to-leaf path 4->9->1 represents the number 491.
# The root-to-leaf path 4->0 represents the number 40.
# Therefore, sum = 495 + 491 + 40 = 1026.
# """




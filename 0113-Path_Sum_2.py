from __future__ import annotations
from timeit import timeit
from functools import partial


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""
sum_=22
    pathSum1:  0.000005 seconds
    pathSum2:  0.000007 seconds
    pathSum3:  0.000005 seconds

sum_=25
    pathSum1:  0.000018 seconds
    pathSum2:  0.000023 seconds
    pathSum3:  0.000022 seconds

sum_=22
    pathSum1:  0.000007 seconds
    pathSum2:  0.000012 seconds
    pathSum3:  0.000009 seconds
"""

solutions = []

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        ans = []
        self.dfs(root, sum, [], ans)

        return ans
        # print(ans)

    def dfs(self, node, sum_, path, ans):
        if node:
            if sum_ == node.val and not node.left and not node.right:
                ans.append(path+[node.val])
            self.dfs(node.left, sum_-node.val, path+[node.val], ans)
            self.dfs(node.right, sum_-node.val, path+[node.val], ans)

solutions.append(("pathSum1", Solution().pathSum))


class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        ans, stack = [], [(root, sum, [])]

        while stack:
            node, sum_, path = stack.pop()
            if node:
                if sum_ == node.val and not node.left and not node.right:
                    ans.append(path+[node.val])
                stack.append((node.right, sum_-node.val, path+[node.val]))
                stack.append((node.left, sum_-node.val, path+[node.val]))

        return ans
        # print(ans)

solutions.append(("pathSum2", Solution().pathSum))


from collections import deque

class Solution:
    def pathSum(self, root: TreeNode, sum: int) -> List[List[int]]:
        ans, queue = [], deque([(root, sum, [])])

        while queue:
            node, sum_, path = queue.popleft()
            if node:
                if sum_ == node.val and not node.left and not node.right:
                    ans.append(path+[node.val])
                    continue
                queue.append((node.left, sum_-node.val, path+[node.val]))
                queue.append((node.right, sum_-node.val, path+[node.val]))

        return ans
        # print(ans)

solutions.append(("pathSum3", Solution().pathSum))

for (root, sum_, number) in (TreeNode(5, TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))),\
                             TreeNode(8, TreeNode(13), TreeNode(4, TreeNode(5), TreeNode(1)))),\
                             22, 10**7),\
                            (TreeNode(5, TreeNode(4, TreeNode(11, TreeNode(7, TreeNode(19), TreeNode(10)),\
                             TreeNode(2, TreeNode(9), TreeNode(3))), TreeNode(20, TreeNode(25, TreeNode(27),\
                             TreeNode(14)), TreeNode(12, TreeNode(17), TreeNode(3)))), TreeNode(8, TreeNode(13,\
                             TreeNode(22, TreeNode(29), TreeNode(12)), TreeNode(10, TreeNode(28), TreeNode(11))),\
                             TreeNode(4, TreeNode(5, TreeNode(9), TreeNode(3)), TreeNode(1, TreeNode(10), TreeNode(2))))),\
                             25, 10),\
                            (TreeNode(5, TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))),\
                             TreeNode(8, TreeNode(13), TreeNode(4, TreeNode(5), TreeNode(1)))),\
                             22, 10):
    text = "\nsum_={}"
    print(text.format(sum_))
    for name, func in solutions:
        t = timeit(partial(func, root, sum_), number=number) / number
        print("  %10s:  %8f seconds" % (name, t))


# test = Solution()
# test.pathSum(TreeNode(5, TreeNode(4, TreeNode(11, TreeNode(7), TreeNode(2))),\
#              TreeNode(8, TreeNode(13), TreeNode(4, TreeNode(5), TreeNode(1)))),\
#              22)
"""
[
   [5,4,11,2],
   [5,8,4,5]
]
"""

from __future__ import annotations
from timeit import timeit
from functools import partial


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

"""
p=<__main__.TreeNode object at 0x1098eca30>
             Recursion:  0.000001 seconds
     Shorter Recursion:  0.000001 seconds
             Iteration:  0.000002 seconds
              Tupleify:  0.000002 seconds

p=<__main__.TreeNode object at 0x109920ca0>
             Recursion:  0.000004 seconds
     Shorter Recursion:  0.000008 seconds
             Iteration:  0.000010 seconds
              Tupleify:  0.000009 seconds

p=<__main__.TreeNode object at 0x109924670>
             Recursion:  0.000003 seconds
     Shorter Recursion:  0.000003 seconds
             Iteration:  0.000004 seconds
              Tupleify:  0.000003 seconds
"""

solutions = []

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if not p and not q:
            return True

        if not p or not q:
            return False

        if p.val != q.val:
            return False

        return self.isSameTree(p.right, q.right) and \
               self.isSameTree(p.left, q.left)
        # print(self.isSameTree(p.right, q.right) and \
        #       self.isSameTree(p.left, q.left))

solutions.append(("Recursion", Solution().isSameTree))


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        if p and q:
            return p.val == q.val and self.isSameTree(p.left, q.left)\
                                  and self.isSameTree(p.right, q.right)

        return p is q
        # True if p == None and q == None else False.

solutions.append(("Shorter Recursion", Solution().isSameTree))


from collections import deque

class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        def check(p, q):
            if not p and not q:
                return True

            if not p or not q:
                return False

            if p.val != q.val:
                return False

            return True

        deq = deque([(p,q),])

        while deq:
            p, q = deq.popleft()

            if not check(p,q):
                return False
                # print(False)
                # return

            if p:
                deq.append((p.left, q.left))
                deq.append((p.right, q.right))

        return True
        # print(True)

solutions.append(("Iteration", Solution().isSameTree))


class Solution:
    def isSameTree(self, p: TreeNode, q: TreeNode) -> bool:
        def tupleify(n):
            return n and (n.val, tupleify(n.left), tupleify(n.right))

        return tupleify(p) == tupleify(q)
        # print(tupleify(p) == tupleify(q))

solutions.append(("Tupleify", Solution().isSameTree))


for (p, q, number) in (TreeNode(1, TreeNode(2), TreeNode(3)), TreeNode(1, TreeNode(2), TreeNode(3)), 10**7),\
                      (TreeNode(25, TreeNode(20, TreeNode(10, TreeNode(5), TreeNode(12)), TreeNode(22)), TreeNode(36, TreeNode(30, TreeNode(28)), TreeNode(40, TreeNode(38), TreeNode(48)))),\
                       TreeNode(25, TreeNode(20, TreeNode(10, TreeNode(5), TreeNode(12)), TreeNode(22)), TreeNode(36, TreeNode(30, TreeNode(28)), TreeNode(40, TreeNode(38), TreeNode(48)))),\
                       10),\
                      (TreeNode(1, TreeNode(2), TreeNode(3)), TreeNode(1, TreeNode(2), TreeNode(3)), 10):
    text = "\np={}"
    print(text.format(p))
    for name, func in solutions:
        t = timeit(partial(func, p, q), number=number) / number
        print("  %20s:  %8f seconds" % (name, t))


# test = Solution()
# test.isSameTree(TreeNode(1, TreeNode(2), TreeNode(3)),\
#                 TreeNode(1, TreeNode(2), TreeNode(3)))
# # True

# test = Solution()
# test.isSameTree(TreeNode(1, TreeNode(2)), TreeNode(1, None, TreeNode(2)))
# # False

# test = Solution()
# test.isSameTree(TreeNode(1, TreeNode(2), TreeNode(1)),\
#                 TreeNode(1, TreeNode(1), TreeNode(2)))
# # False

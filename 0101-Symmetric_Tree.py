from __future__ import annotations


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        def isMirror(t1, t2):
            if t1 == None and t2 == None: return True
            if t1 == None or t2 == None: return False

            return t1.val == t2.val\
               and isMirror(t1.left, t2.right)\
               and isMirror(t1.right, t2.left)

        return isMirror(root, root)
        # print(isMirror(root, root))


from collections import deque

class Solution:
    def isSymmetric(self, root: TreeNode) -> bool:
        if root == None: return True

        def isValid(t1, t2):
            if not t1 and not t2:
                return True

            if not t1 or not t2:
                return False

            if t1.val != t2.val:
                return False

            return True

        deq = deque([(root.left, root.right),])

        while deq:
            t1, t2 = deq.popleft()
            if not isValid(t1, t2):
                return False
            if t1 or t2:
                deq.append((t1.left, t2.right))
                deq.append((t2.left, t1.right))

        return True


test = Solution()
test.isSymmetric(TreeNode(1, TreeNode(2, TreeNode(3), TreeNode(4)),\
                         TreeNode(2, TreeNode(4), TreeNode(3))))
# True

test = Solution()
test.isSymmetric(TreeNode(1, TreeNode(2, None, TreeNode(3)),\
                         TreeNode(2, None, TreeNode(3))))
# False

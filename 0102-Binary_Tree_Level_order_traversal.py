from __future__ import annotations


class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []

        ans = []
        self.traverse(root, 1, ans)

        return ans
        # print(ans)

    def traverse(self, node, level, ans):
        if not node: return

        if level > len(ans): # Then you are at a new level
            ans.append([node.val])
        else:
            ans[level-1].extend([node.val])

        self.traverse(node.left, level+1, ans)
        self.traverse(node.right, level+1, ans)


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        ans, level = [], [root]

        while root and level:
            currNodes, nextLevel = [], []
            for node in level:
                currNodes.append(node.val)
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)

            ans.append(currNodes)
            level = nextLevel

        return ans
        # print(ans)


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        if not root: return []

        ans, level = [], [root]

        while level:
            ans.append([node.val for node in level])
            temp = []
            for node in level:
                temp.extend([node.left, node.right])
            level = [leaf for leaf in temp if leaf]

        return ans
        # print(ans)


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        ans, level = [], [root]

        while root and level:
            ans.append([node.val for node in level])
            pair = [(node.left, node.right) for node in level]
            level = [leaf for LR in pair for leaf in LR if leaf]

        return ans
        # print(ans)


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        ans, level = [], [root]

        while root and level:
            ans.append([node.val for node in level])
            pair = [(node.left, node.right) for node in level]
            level = [child for n in level\
                     for child in (n.left, n.right) if child]

        return ans
        # print(ans)


class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        hmap = {}

        def levOrd(node, level):
            if not node: return

            hmap.setdefault(level, []).append(node.val)
            levOrd(node.left, level+1)
            levOrd(node.right, level+1)

        levOrd(root, 0)

        return list(hmap.values())
        # print(list(hmap.values()))


# This is the kind of solution good for vertical order tree traversa
from collections import deque
class Solution:
    def levelOrder(self, root: TreeNode) -> List[List[int]]:
        que = deque([(0, root)])
        vals = {}

        while que:
            level, node = que.popleft()
            if node:
                vals[level] = vals.get(level, []) + [node.val]
                que += (level+1, node.left), (level+1, node.right)

        return [vals[level] for level in sorted(vals)]
        # print([vals[level] for level in sorted(vals)])


test = Solution()
test.levelOrder(TreeNode(3, TreeNode(9),\
               TreeNode(20, TreeNode(15), TreeNode(7))))
"""
[
  [3],
  [9,20],
  [15,7]
]
"""

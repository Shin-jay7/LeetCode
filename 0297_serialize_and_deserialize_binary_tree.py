from __future__ import annotations


class TreeNode():
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None


class Codec:
    def serialize(self, root):
        if not root:
            return '#'

        return ','.join([str(root.val), self.serialize(root.left), self.serialize(root.right)])

    def deserialize(self, data):
        self.data = data
        if self.data[0] == '#':
            return None
        node = TreeNode(self.data[:self.data.find(',')])
        node.left = self.deserialize(self.data[self.data.find(',')+1:])
        node.right = self.deserialize(self.data[self.data.find(',')+1:])

        return node


class Codec:
    def serialize(self, root):
        def execute(node):
            if node:
                vals.append(str(node.val))
                execute(node.left)
                execute(node.right)
            else:
                vals.append('#')

        vals = []
        execute(root)
        return ' '.join(vals)

    def deserialize(self, data):
        def execute():
            val = next(vals)
            if val == '#':
                return None
            node = TreeNode(int(val))
            node.left = execute()
            node.right = execute()
            return node

        vals = iter(data.split())
        return execute()

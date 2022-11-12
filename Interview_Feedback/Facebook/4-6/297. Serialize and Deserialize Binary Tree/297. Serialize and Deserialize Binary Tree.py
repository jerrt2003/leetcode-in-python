# -*- coding: utf-8 -*-
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:
    """
    pre-order traversal
    """

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        self.res = []
        self._serialize(root)
        return ','.join(self.res)

    def _serialize(self, node):
        if not node:
            self.res.append('x')
            return
        self.res.append(str(node.val))
        self._serialize(node.left)
        self._serialize(node.right)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        self.data = data.split(',')
        return self._deserialize()

    def _deserialize(self):
        current = self.data.pop(0)
        if current == 'x':
            return None
        node = TreeNode(int(current))
        node.left = self._deserialize()
        node.right = self._deserialize()
        return node


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
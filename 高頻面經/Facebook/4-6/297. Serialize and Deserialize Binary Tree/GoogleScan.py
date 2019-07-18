# -*- coding: utf-8 -*-
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        self.output = []
        self._serialize(root)
        return ','.join(self.output)

    def _serialize(self, root):
        if root is None:
            self.output.append('X')
            return
        self.output.append(str(root.val))
        if root.left:
            self._serialize(root.left)
        if root.right:
            self._serialize(root.right)



    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        data = data.split(',')
        return self._deserialize(data)

    def _deserialize(self, data):
        if not data:
            return
        val = data.pop(0)
        if val == 'X':
            return None
        root = TreeNode(val)
        root.left = self._deserialize(data)
        root.right = self._deserialize(data)
        return root

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
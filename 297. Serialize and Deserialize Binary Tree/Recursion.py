# -*- coding: utf-8 -*-
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:
    """
    Solution: Recursion
    Time Complexity:
    Space Complexity:
    Inspired By: MYSELF !!
    Thinking process:
    - Serialize:
        - Do preOrderTraversal to convert tree into a string
        - If hit None, then we use char 'X' to stand for None (thus we know when to end when do deserialize later)
        - We'll use ',' to denote split function
    - De-serialize:
        - first we divide the string by ',' -> we'll get a list
        - start pop from beginning of the list
        - If we hit 'X' we know its a None in original tree -> so we return None
    """

    def __init__(self):
        self.res = ''

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        def preOrderTraversal(root=None):
            if root is None:
                self.res += 'X' + ','
                return
            self.res += str(root.val) + ','
            preOrderTraversal(root.left)
            preOrderTraversal(root.right)
        preOrderTraversal(root)
        return self.res

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if data is None or len(data) == 0: return None
        data = data.split(',')

        def buildTree(data):
            tmp = data.pop(0)
            if tmp == 'X': return None
            node = TreeNode(tmp)
            node.left = buildTree(data)
            node.right = buildTree(data)
            return node

        return buildTree(data)


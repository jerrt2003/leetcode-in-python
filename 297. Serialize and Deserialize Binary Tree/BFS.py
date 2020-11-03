# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
import collections


class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.
        Facebook
        BFS
        T:O(n) S:O(n)
        Runtime: 164 ms, faster than 36.78% of Python online submissions for Serialize and Deserialize Binary Tree.
        Memory Usage: 23.2 MB, less than 23.73% of Python online submissions for Serialize and Deserialize Binary Tree.
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return ""
        data = []
        q = collections.deque([root])
        while q:
            node = q.popleft()
            if node:
                q.append(node.left)
                q.append(node.right)
            data.append(node.val if node else "X")
        return ",".join(str(c) for c in data)

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        data = data.split(",")
        root = TreeNode(int(data[0]))
        idx = 1
        q = collections.deque([root])
        while q:
            node = q.popleft()
            if data[idx] != "X":
                left_node = TreeNode(int(data[idx]))
                node.left = left_node
                q.append(left_node)
            idx += 1
            if data[idx] != "X":
                right_node = TreeNode(int(data[idx]))
                node.right = right_node
                q.append(right_node)
            idx += 1
        return root









# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Codec:

    def serialize(self, root):
        """Encodes a tree to a single string.

        :type root: TreeNode
        :rtype: str
        """
        ret = []

        def dfs(node):
            if not node:
                return
            ret.append(node.val)
            if node.left:
                dfs(node.left)
            else:
                ret.append('X')
            if node.right:
                dfs(node.right)
            else:
                ret.append('X')

        dfs(root)
        return ",".join([str(a) for a in ret])

    def deserialize(self, data):
        """Decodes your encoded data to tree.

        :type data: str
        :rtype: TreeNode
        """
        if len(data) == 0:
            return
        data = data.split(",")

        def dfs(data):
            curr = data.pop(0)
            if curr == 'X':
                return None
            root = TreeNode(int(curr))
            root.left = dfs(data)
            root.right = dfs(data)
            return root

        return dfs(data)

# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.deserialize(codec.serialize(root))
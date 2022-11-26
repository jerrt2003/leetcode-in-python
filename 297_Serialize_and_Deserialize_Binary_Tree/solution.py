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
        if not root:
            return ""
        nodes = []
        q = [root]
        while q:
            node = q.pop(0)
            if node:
                nodes.append(node.val)
                q.append(node.left)
                q.append(node.right)
            else:
                nodes.append('X')
        return ",".join(str(c) for c in nodes)

    def deserialize(self, data):
        """Decodes your encoded data to tree.
        
        :type data: str
        :rtype: TreeNode
        """
        if not data:
            return None
        data = data.split(",")
        root = TreeNode(data[0])
        q = [root]
        idx = 1
        while idx < len(data):
            node = q.pop(0)
            if data[idx] != 'X':
                left_node = TreeNode(data[idx])
                node.left = left_node
                q.append(left_node)
            idx += 1
            if data[idx] != 'X':
                right_node = TreeNode(data[idx])
                node.right = right_node
                q.append(right_node)
            idx += 1
        return root

        

        

# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# ans = deser.deserialize(ser.serialize(root))
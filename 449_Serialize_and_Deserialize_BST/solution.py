from typing import Optional, List

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Codec:

    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string.
        """
        # preorder: root -> left -> right
        # all left node(s) value < root.val
        # all right node(s) value > root.val
        def _serialize(root: TreeNode):
            node_values.append(root.val)
            if root.left:
                _serialize(root.left)
            if root.right:
                _serialize(root.right)

        node_values: List[int] = []
        if root:
            _serialize(root)
        
        return ",".join([str(v) for v in node_values])
        

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree.
        """
        def _deserialize(data: List[int]) -> Optional[TreeNode]:
            if not data:
                return None
            root = TreeNode(data[0])
            root.left = _deserialize([v for v in data if v < data[0]])
            root.right = _deserialize([v for v in data if v > data[0]])
            return root

        data = [int(v) for v in data.split(",")]
        return _deserialize(data)


        

# Your Codec object will be instantiated and called as such:
# Your Codec object will be instantiated and called as such:
# ser = Codec()
# deser = Codec()
# tree = ser.serialize(root)
# ans = deser.deserialize(tree)
# return ans
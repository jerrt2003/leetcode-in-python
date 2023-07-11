from typing import List, Optional
from common.tree_node import TreeNode


class Solution:
    def boundaryOfBinaryTree(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
        ans = [root.val]
        if not root.left and not root.right:
            return ans
        if root.left:
            ans += self.find_left_boundary(root.left)
        ans += self.find_leaf_node(root)
        if root.right:
            ans += self.find_right_boundary(root.right)[::-1]

        return ans

    def find_left_boundary(self, node) -> List[int]:
        if not node.left and not node.right:
            return []
        ret = [node.val]
        if node.left:
            return ret + self.find_left_boundary(node.left)
        else:
            return ret + self.find_left_boundary(node.right)

    def find_right_boundary(self, node) -> List[int]:
        if not node.left and not node.right:
            return []
        ret = [node.val]
        if node.right:
            return ret + self.find_right_boundary(node.right)
        else:
            return ret + self.find_right_boundary(node.left)

    def find_leaf_node(self, node) -> List[int]:
        if not node.left and not node.right:
            return [node.val]
        ret = []
        if node.left:
            ret += self.find_leaf_node(node.left)
        if node.right:
            ret += self.find_leaf_node(node.right)
        return ret

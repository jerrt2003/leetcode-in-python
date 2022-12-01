from typing import Optional, List, Tuple

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        # return self.helper(root, None, None)
        return self.helper(root)

        

    # def helper(self, root: Optional[TreeNode], min_node: Optional[TreeNode], max_node: Optional[TreeNode]) -> bool:
    #     if not root:
    #         return True
    #     # 首先，当前节点的值不能小于最小值，不能大于最大值（左子节点无最小值限制，最大值为当前节点值；右节点无最大值，限制最小值为当前节点值）            
    #     if min_node and root.val <= min_node.val:
    #         return False
    #     if max_node and root.val >= max_node.val:
    #         return False
    #     return self.helper(root.left, min_node, root) and self.helper(root.right, root, max_node)

    def helper(self, root: Optional[TreeNode]) -> bool:
        prev: Optional[int] = None
        stack: List[Tuple[TreeNode, int]] = [(root, 1)]
        while stack:
            node, color = stack.pop()
            if color == 0:
                if prev is not None and node.val <= prev:
                    return False
                prev = node.val
            else:
                if node.right:
                    stack.append((node.right, 1))
                stack.append((node, 0))
                if node.left:
                    stack.append((node.left, 1))
        return True
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return self.helper(root, root)

    # recursion
    # def helper(self, left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
    #     if not left and not right:
    #         return True
    #     elif left and right:
    #         return left.val == right.val and self.helper(left.left, right.right) and self.helper(left.right, right.left)
    #     else:
    #         return False

    # interactive
    def helper(self, left: Optional[TreeNode], right: Optional[TreeNode]) -> bool:
        q = [left, right]
        while q:
            node_1 = q.pop(0)
            node_2 = q.pop(0)
            if not node_1 and not node_2:
                continue
            elif node_1 and node_2:
                if node_1.val != node_2.val:
                    return False
                q.append(node_1.left)
                q.append(node_2.right)
                q.append(node_1.right)
                q.append(node_2.left)
            else:
                return False
        return True
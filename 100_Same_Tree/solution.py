from typing import Optional, List, Tuple

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        return self.helper(p, q)

    # recursion: 遞歸
    # def helper(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
    #     if not p and not q:
    #         return True
    #     if p and q:
    #         if p.val != q.val:
    #             return False
    #         return self.helper(p.left, q.left) and self.helper(p.right, q.right)
    #     else:
    #         return False

    # interactive: 迭代
    def helper(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        p_stack: List[Tuple(TreeNode, int)] = [(p, 1)]
        q_stack: List[Tuple(TreeNode, int)] = [(q, 1)]
        while p_stack and q_stack:
            p_node, p_color = p_stack.pop()
            q_node, q_color = q_stack.pop()
            if p_color == 1 and q_color == 1:
                if p_node.val != q_node.val:
                    return False
            elif p_color == 0 and q_color == 0:
                p_stack.append((p_node.left, 0))
                p_stack.append((p_node, 1))
                p_stack.append((p_node.right, 0))
                q_stack.append((q_node.left, 0))
                q_stack.append((q_node, 1))
                q_stack.append((q_node.right, 0))
            else:
                return False

        return not p_stack and not q_stack

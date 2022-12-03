# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        return self.helper(root, p, q)
        
        
    def helper(self, node: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
        if not node:
            return None
        if node.val == p.val or node.val == q.val:
            return node
        ret_left = self.helper(node.left, p, q)
        ret_right = self.helper(node.right, p, q)
        # 当 left 和 right 同时不为空 ：说明 p, q分列在 root 的 异侧 （分别在 左 / 右子树），因此 root 为最近公共祖先，返回 root
        if ret_left and ret_right:
            return node
        # 当 left 不为空 ， right 为空: p,q都不在 root 的右子树中，直接返回 left
        elif ret_left:
            return ret_left
        # 当 left 为空 ，right 不为空 ：p,q都不在 root 的左子树中，直接返回 right
        elif ret_right:
            return ret_right
        # 当 left 和 right 同时为空 ：说明 root 的左 / 右子树中都不包含 p,q ，返回 null
        return None
        
        
        
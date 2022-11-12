# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def delNodes(self, root, to_delete):
        """
        DFS
        T:O(n) S:O(n)
        Runtime: 64 ms, faster than 51.02% of Python online submissions for Delete Nodes And Return Forest.
        Memory Usage: 13.2 MB, less than 100.00% of Python online submissions for Delete Nodes And Return Forest.
        :type root: TreeNode
        :type to_delete: List[int]
        :rtype: List[TreeNode]
        """
        ret = []
        to_delete = set(to_delete)
        def dfs(node):
            if not node:
                return None
            node.left = dfs(node.left)
            node.right = dfs(node.right)
            if node.val in to_delete:
                if node.left:
                    ret.append(node.left)
                if node.right:
                    ret.append(node.right)
                return None
            return node

        dfs(root)
        if root.val not in to_delete:
            ret.append(root)
        return ret



# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def minCameraCover(self, root):
        """
        T:O(n) S:O(1)
        Runtime: 36 ms, faster than 55.56% of Python online submissions for Binary Tree Cameras.
        Memory Usage: 13.4 MB, less than 10.00% of Python online submissions for Binary Tree Cameras.
        :type root: TreeNode
        :rtype: int
        """
        # 0: leaf node
        # 1: cover w/ camera
        # 2: cover w/o camera
        self.res = 0
        def dfs(node):
            if not node: return 2
            l, r = dfs(node.left), dfs(node.right)
            if l == 0 or r == 0:
                self.res += 1
                return 1
            return 2 if l == 1 or r == 1 else 0
        r = dfs(root)
        if r == 0: return 1 + self.res
        return self.res
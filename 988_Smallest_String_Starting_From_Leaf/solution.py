# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def smallestFromLeaf(self, root):
        """
        T:O(n) S:O(1)
        Runtime: 32 ms, faster than 94.09% of Python online submissions for Smallest String Starting From Leaf.
        Memory Usage: 16 MB, less than 40.11% of Python online submissions for Smallest String Starting From Leaf.
        :type root: TreeNode
        :rtype: str
        """
        self.min_str = None

        def dfs(path, node):
            if not node.left and not node.right:
                if self.min_str is None or chr(ord('a')+node.val) + path < self.min_str:
                    self.min_str = chr(ord('a')+node.val) + path
                    return
            if node.left:
                dfs(chr(ord('a')+node.val) + path, node.left)
            if node.right:
                dfs(chr(ord('a')+node.val) + path, node.right)

        dfs('', root)
        return self.min_str
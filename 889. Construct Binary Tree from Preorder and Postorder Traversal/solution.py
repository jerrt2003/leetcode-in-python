# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def constructFromPrePost(self, pre, post):
        """
        Tree
        T:O(N) S:O(1)
        Runtime: 44 ms, faster than 57.21% of Python online submissions for Construct Binary Tree from Preorder and Postorder Traversal.
        Memory Usage: 12.6 MB, less than 100.00% of Python online submissions for Construct Binary Tree from Preorder and Postorder
        :type pre: List[int]
        :type post: List[int]
        :rtype: TreeNode
        """
        if not pre:
            return None
        val = pre[0]
        root = TreeNode(val)
        if len(pre) == 1:
            return root
        L = post.index(val) + 1
        root.left = self.constructFromPrePost(pre[:L+1], post[:L])
        root.right = self.constructFromPrePost(pre[L+1:], post[L:-1])
        return root

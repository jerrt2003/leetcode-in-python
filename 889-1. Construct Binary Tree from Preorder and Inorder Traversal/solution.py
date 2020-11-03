# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def constructFromPrePost(self, preorder, inorder):
        """
        Facebook
        :type pre: List[int]
        :type post: List[int]
        :rtype: TreeNode
        """
        if not preorder and not inorder:
            return None
        curr = preorder.pop(0)
        new_node = TreeNode(val=curr)
        idx = inorder.index(curr)
        new_node.left = self.constructFromPrePost(preorder[:idx], inorder[:idx])
        new_node.right = self.constructFromPrePost(preorder[idx:], inorder[idx+1:])
        return new_node



node = Solution().constructFromPrePost([1,2,4,5,3,6],[4,2,5,1,3,6])
print node
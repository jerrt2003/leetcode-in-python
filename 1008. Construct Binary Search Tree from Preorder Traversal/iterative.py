# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def bstFromPreorder(self, preorder):
        """
        Facebook
        T:O(n) S:O(n)
        Runtime: 28 ms, faster than 58.53% of Python online submissions for Construct Binary Search Tree from Preorder Traversal.
        Memory Usage: 12.7 MB, less than 97.39% of Python online submissions for Construct Binary Search Tree from Preorder Traversal.
        :type preorder: List[int]
        :rtype: TreeNode
        """
        if not preorder:
            return None

        root = TreeNode(preorder[0])
        stack = [root]

        for i in range(1, len(preorder)):
            parent, child = stack[-1], TreeNode(preorder[i])
            while stack and stack[-1].val < child.val:
                parent = stack.pop()

            if parent.val < child.val:
                parent.right = child
            else:
                parent.left = child

            stack.append(child)

        return root
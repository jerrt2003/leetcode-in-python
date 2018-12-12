# -*- coding: utf-8 -*-
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def buildTree(self, preorder, inorder):
        """
        Solution: Recursion
        Time Complexity:
        Space Complexity:
        Inspired By:
            https://leetcode.com/problems/construct-binary-tree-from-preorder-and-inorder-traversal/discuss/34579/Python-short-recursive-solution
            http://leetcode.com/2011/04/construct-binary-tree-from-inorder-and-preorder-postorder-traversal.html
        Thinking process:
            - preorder-traversal: root -> left -> right (rule 1)
            - inorder-traversal: left -> root -> right (rule 2)
            - pop the first element x in porder: it must be the root for the tree (rule 1)
            - Find idx of x in inorder list, then:
                - (rule 2)
                - inorder[:i] must be in the left side of tree
                - inorder[i+1:] must be in the right side of tree
            - continue this recursive logic till (divided) inorder tree is None then return None (no more nodes need to construct)
        :type inorder: List[int]
        :rtype: TreeNode
        """
        if len(inorder) == 0 or inorder is None:
            return None
        root = TreeNode(preorder.pop(0))
        idx = inorder.index(root.val)
        # 為什麼需要帶入preorder?
        # 因為(rule1)preorder下一個數必為root.left的root node
        root.left = self.buildTree(preorder, inorder[:idx])
        root.right = self.buildTree(preorder, inorder[idx+1:])
        return root

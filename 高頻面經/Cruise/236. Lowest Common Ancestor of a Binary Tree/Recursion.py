# -*- coding: utf-8 -*-
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        Solution: Recursion
        Time Complexity:
        Space Complexity:
        Inspired By: https://leetcode.com/problems/lowest-common-ancestor-of-a-binary-tree/discuss/65226/My-Java-Solution-which-is-easy-to-understand
        Thinking Process:
        Algorithm:
        if root is None or root.val = p or root.val = q: #表示有找到p或q,則回傳root, 若是root is None則回傳None
            return root
        left = lowestCommonAncestor(root.left,p,q) 找左邊的樹
        right = lowestCommonAncestor(root.right,p,q) 找右邊的樹
        if left is not None and right is not None: 表示兩邊的樹都有找到數字,又在此BT裡面的數都為unique所以可以判斷root為lowest ancestor
            return root
        if left is not None: return left #只要左邊樹或是右邊樹有找到數值,則回傳該子節點,不然就回傳None(表示找不到)
        return right
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        # 為什麼當root.val只需要是p或是q的其中之一我們就可以回傳了呢？(假設我們已經找到p)
        # 因為一旦我們回傳,下一步就是找父節點的right node
        # 若是right is not None, 表示q在right side,所以LCA為父節點
        # 若是right is None, 表示就會是p的子節點(因為p,q一定都會在樹裡面),所以left為LCA
        if root is None or root.val in [p.val,q.val]:
            return root
        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)
        if left is not None and right is not None:
            return root
        if left is not None:
            return left
        return right
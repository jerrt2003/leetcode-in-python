# -*- coding: utf-8 -*-
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def __init__(self):
        self.first_element = None
        self.second_element = None
        self.prev_element = TreeNode(-float('inf'))

    def recoverTree(self, root):
        """
        Solution: Recursion(inorder traverse)
        Time Complexity:
        Space Complexity:
        Inspired By: https://leetcode.com/problems/recover-binary-search-tree/discuss/32535/No-Fancy-Algorithm-just-Simple-and-Powerful-In-Order-Traversal
        Thinking Process:
        - inorder traverse: left -> root -> right
        - In BST, inorder traverse is useful because left < root < right
        - So let's do inorder traverse to find those "2" elements which mis-placed (first_element, second_element):
            - define a pre_element (it will store the previous element we visit so we can compare)
            - if first_element is None and pre_element.val >= cur.val:
                - we find the first mis-placed element
                - first_element = pre_element
            - if first_element is not None and pre.val >= cur.val:
                - if first_element is found, then this time it must be the 2nd element
                - second_element = cur (note: this time the cur element is the one mis-placed)
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """
        self.inOrderTraverse(root)
        # now we found the first and second element, let's replace their value
        tmp = self.first_element.val
        self.first_element.val = self.second_element.val
        self.second_element.val = tmp


    def inOrderTraverse(self, root=None):
        if root is None: return
        self.inOrderTraverse(root.left)
        if self.first_element is None and self.prev_element.val >= root.val:
            self.first_element = self.prev_element
        if self.first_element is not None and self.prev_element.val >= root.val:
            self.second_element = root
        self.prev_element = root
        self.inOrderTraverse(root.right)

node_1 = TreeNode(1)
node_2 = TreeNode(2)
node_3 = TreeNode(3)
node_4 = TreeNode(4)
node_3.left = node_1
node_3.right = node_4
node_4.left = node_2

sol = Solution()
sol.recoverTree(node_3)


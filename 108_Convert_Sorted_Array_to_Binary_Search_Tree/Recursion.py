# -*- coding: utf-8 -*-
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        Solution: Recursion
        Time Complexity:
        Space Complexity:
        Inspired By: https://leetcode.com/problems/convert-sorted-array-to-binary-search-tree/discuss/35223/An-easy-Python-solution
        Thinking process:
        - Find the mid point of the list and make it as root
        - then convert left side of list
        - then convert right side of list
        - return root node
        Algorithm:
        def convert(nums):
            if nums is None: <- means we can divide the list by 2 anymore thus return None
                return None
            mid = len(nums)/2
            root = TreeNode(nums[mid])
            root.left = convert(nums[:mid])
            root.right = convert(nums[mid:len(nums)]
            return root
        :type nums: List[int]
        :rtype: TreeNode
        """
        def convert(nums):
            if len(nums) == 0: return None
            mid = len(nums)/2
            root = TreeNode(nums[mid])
            root.left = convert(nums[:mid])
            root.right = convert(nums[mid+1:len(nums)]) # need to use mid+1 for right side starting point
            return root

        return convert(nums)
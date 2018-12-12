# -*- coding: utf-8 -*-
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        Solution: Recursion
        Time Complexity: O(n^2)
        Space Complexity:
        Inspired By:
        Thinking process:
        - Find the index for the maximum number of array
        - divide the array into 2 parts a, b
        - continue to find the maximum tree for a, b till no more number left
        :type nums: List[int]
        :rtype: TreeNode
        """
        def findMaxTree(nums):
            if len(nums) == 0: return None
            #max_num_idx = nums.index(sorted(nums)[-1])
            max_num_idx = nums.index(max(nums)) # this will improve execution speed
            node = TreeNode(nums[max_num_idx])
            node.left = findMaxTree(nums[:max_num_idx])
            node.right = findMaxTree(nums[max_num_idx+1:])
            return node

        return findMaxTree(nums)

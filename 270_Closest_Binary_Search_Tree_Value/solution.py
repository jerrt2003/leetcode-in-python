# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def closestValue(self, root, target):
        """
        Facebook
        Runtime: 36 ms, faster than 49.93% of Python online submissions for Closest Binary Search Tree Value.
        Memory Usage: 17 MB, less than 15.22% of Python online submissions for Closest Binary Search Tree Value.
        T:O(k) S:O(n)
        :type root: TreeNode
        :type target: float
        :rtype: int
        """
        min_val = float('inf')
        ans = None
        node = root
        while node:
            if abs(node.val - target) < min_val:
                min_val = abs(node.val - target)
                ans = node.val
            if node.val > target:
                node = node.left
            else:
                node = node.right

        return ans


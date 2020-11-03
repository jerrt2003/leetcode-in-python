# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def getAllElements(self, root1, root2):
        """
        Facebook
        Iterative in-order traversal
        T:O(n) S:O(n)
        Runtime: 452 ms, faster than 44.38% of Python online submissions for All Elements in Two Binary Search Trees.
        Memory Usage: 19 MB, less than 80.88% of Python online submissions for All Elements in Two Binary Search Trees.
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: List[int]
        """
        stack1, stack2, ans = [], [], []
        while root1 or root2 or stack1 or stack2:
            while root1:
                stack1.append(root1)
                root1 = root1.left
            while root2:
                stack2.append(root2)
                root2 = root2.left

            if not stack2 or (stack1 and stack1[-1].val <= stack2[-1].val):
                root1 = stack1.pop()
                ans.append(root1.val)
                root1 = root1.right
            else:
                root2 = stack2.pop()
                ans.append(root2.val)
                root2 = root2.right
        return ans
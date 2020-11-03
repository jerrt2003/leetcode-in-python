# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections


class Solution(object):
    def findTarget(self, root, k):
        """
        Facebook
        T:O(n) S:O(n)
        Runtime: 64 ms, faster than 93.87% of Python online submissions for Two Sum IV - Input is a BST.
        Memory Usage: 17.3 MB, less than 43.71% of Python online submissions for Two Sum IV - Input is a BST.
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        bst, seen = collections.deque([root]), set()
        while bst:
            curr = bst.popleft()
            if k - curr.val in seen:
                return True
            else:
                seen.add(curr.val)
                if curr.left:
                    bst.append(curr.left)
                if curr.right:
                    bst.append(curr.right)

        return False
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next
"""


class Solution(object):
    def connect(self, root):
        """
        Facebook
        T:O(n) S:O(1)
        Runtime: 56 ms, faster than 72.27% of Python online submissions for Populating Next Right Pointers in Each Node.
        Memory Usage: 15.7 MB, less than 52.35% of Python online submissions for Populating Next Right Pointers in Each Node.
        :type root: Node
        :rtype: Node
        """
        if not root:
            return root
        q = [root]
        while q:
            l = len(q)
            for i in range(l):
                curr = q.pop(0)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
                if i != l - 1:
                    curr.next = q[0]
        return root

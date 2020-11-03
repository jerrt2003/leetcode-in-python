
# Definition for a Node.
class Node(object):
    def __init__(self, val=0, left=None, right=None, next=None):
        self.val = val
        self.left = left
        self.right = right
        self.next = next


class Solution(object):
    def connect(self, root):
        """
        Facebook
        T:O(n) S:O(1)
        Runtime: 52 ms, faster than 82.84% of Python online submissions for Populating Next Right Pointers in Each Node.
        Memory Usage: 15.7 MB, less than 97.11% of Python online submissions for Populating Next Right Pointers in Each Node.
        :type root: Node
        :rtype: Node
        """
        if not root:
            return None

        leftmost = root
        while leftmost.left:
            head = leftmost
            while head:
                head.left.next = head.right
                if head.next:
                    head.right.next = head.next.left
                head = head.next
            leftmost = leftmost.left

        return root
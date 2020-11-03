"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
"""

class Solution(object):
    def treeToDoublyList(self, root):
        """
        Facebook
        T:O(n) S:O(n)
        Runtime: 44 ms, faster than 65.59% of Python online submissions for Convert Binary Search Tree to Sorted Doubly Linked List.
        Memory Usage: 13.4 MB, less than 81.92% of Python online submissions for Convert Binary Search Tree to Sorted Doubly Linked List.
        :type root: Node
        :rtype: Node
        """
        if not root:
            return None
        dummy = Node(0)
        prev = dummy
        stack, node = [], root
        while stack or node:
            while node:
                stack.append(node)
                node = node.left
            node = stack.pop()
            node.left, prev.right, prev = prev, node, node
            node = node.right
        dummy.right.left, prev.right = prev, dummy.right
        return dummy.right
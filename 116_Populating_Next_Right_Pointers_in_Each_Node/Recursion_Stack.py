# -*- coding: utf-8 -*-
# Definition for binary tree with next pointer.
class TreeLinkNode:
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.next = None

class Solution:
    # @param root, a tree link node
    # @return nothing
    """
    Solution: Recursion + Queue
    Time Complexity: O(n)
    Space Complexity: O(n)
    Inspired By: MYSELF!!
    Thinking Process:
    - this question is very similar to Q.102
    - we are going to leverage FIFO queue
    """
    def connect(self, root):
        if root is None: return
        starting_queue = [root]
        self.findNextRightLink(starting_queue)

    def findNextRightLink(self, queue):
        queue_for_next_level = []
        while len(queue) != 0:
            node = queue.pop(0)
            if len(queue) != 0:
                node.next = queue[0]
            else:
                node.next = None
            if node.left is not None:
                queue_for_next_level.append(node.left)
            if node.right is not None:
                queue_for_next_level.append(node.right)
        if len(queue_for_next_level) != 0:
            self.findNextRightLink(queue_for_next_level)




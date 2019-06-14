# -*- coding: utf-8 -*-
"""
# Definition for a Node.
class Node(object):
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random
"""
class Solution(object):
    def copyRandomList(self, head):
        """
        Solution: O(n)
        Time Complexity: O(n)
        Space Complexity: O(n)
        Perf: Runtime: 384 ms, faster than 61.01% / Memory Usage: 14.5 MB, less than 86.34%
        :type head: Node
        :rtype: Node
        """
        if not head:
            return None
        copyHead = Node(head.val, None, None)
        maps = dict()
        maps[head] = copyHead
        while head:
            _copyHead = maps[head]
            if head.next not in maps:
                if head.next:
                    copyNext = Node(head.next.val, None, None)
                else:
                    copyNext = None
                maps[head.next] = copyNext
                _copyHead.next = copyNext
            else:
                _copyHead.next = maps[head.next]
            if head.random not in maps:
                if head.random:
                    copyRandom = Node(head.random.val, None, None)
                else:
                    copyRandom = None
                maps[head.random] = copyRandom
                _copyHead.random = copyRandom
            else:
                _copyHead.random = maps[head.random]
            head = head.next
        return copyHead
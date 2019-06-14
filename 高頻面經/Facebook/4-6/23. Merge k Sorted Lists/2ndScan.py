# -*- coding: utf-8 -*-
# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import heapq
class Solution(object):
    def mergeKLists(self, lists):
        """
        Time: O(nlog(k)) n: number of nodes, k: len of lists
        Perf: Runtime: 108 ms, faster than 57.15% / Memory Usage: 17.6 MB, less than 38.93%
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        if not lists:
            return None
        stack = []
        head = ListNode(None)
        start = head
        for node in lists:
            if node:
                heapq.heappush(stack, (node.val, node))
        while stack:
            val, curNode = heapq.heappop(stack)
            head.next = curNode
            if curNode.next:
                heapq.heappush(stack, (curNode.next.val, curNode.next))
            head = head.next
        return start.next

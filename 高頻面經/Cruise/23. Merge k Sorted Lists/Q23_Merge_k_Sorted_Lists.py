# Definition for singly-linked list.
class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

from Queue import PriorityQueue

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        head = ListNode(0)
        curr = head
        q = PriorityQueue()
        for node in lists:
            if node:
                q.put((node.val, node))
        while not q.empty():
            _node = q.get()[1]
            curr.next = _node
            curr = curr.next
            if _node.next:
                q.put((_node.next.val, _node.next))
        return head.next

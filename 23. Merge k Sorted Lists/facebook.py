# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def mergeKLists(self, lists):
        """
        Facebook
        T:O(nlogn) S:O(n)
        Runtime: 100 ms, faster than 83.38% of Python online submissions for Merge k Sorted Lists.
        Memory Usage: 19 MB, less than 61.82% of Python online submissions for Merge k Sorted Lists.
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        dummy = ListNode()
        head = dummy
        pq = []
        for node in lists:
            if node:
                heapq.heappush(pq, (node.val, node))

        while pq:
            _, curr_node = heapq.heappop(pq)
            dummy.next = curr_node
            dummy = dummy.next
            if curr_node.next:
                heapq.heappush(pq, (curr_node.next.val, curr_node.next))

        return head.next


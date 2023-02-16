import heapq

from common.list_node import ListNode
from typing import List, Optional

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        q = []
        heapq.heapify(q)
        for node in lists:
            heapq.heappush(q, node)
        
        dummy = ListNode()
        cur_node = dummy

        while q:
            node = heapq.heappop(q)
            next_node  = node.next
            cur_node.next = node
            cur_node = cur_node.next
            cur_node.next = None
            if next_node:
                heapq.heappush(q, next_node)
        
        return dummy.next

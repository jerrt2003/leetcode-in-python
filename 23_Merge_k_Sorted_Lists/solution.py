from typing import Optional, List
import heapq

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        mini_heap = []
        for i in range(len(lists)):
            mini_heap.append((lists[i].val, i))
        heapq.heapify(mini_heap)

        dummy_node = ListNode()
        curr = dummy_node

        while mini_heap:
            _, node_idx = heapq.heappop(mini_heap)

            # 此處必須將LinkedList Node跟他的下一個node的連結切斷 
            # 不然的話會出現loop
            tmp = lists[node_idx].next
            lists[node_idx].next = None
            curr.next = lists[node_idx]
            curr = curr.next

            if tmp:
                lists[node_idx] = tmp
                heapq.heappush(mini_heap, (lists[node_idx].val, node_idx))

        return dummy_node.next

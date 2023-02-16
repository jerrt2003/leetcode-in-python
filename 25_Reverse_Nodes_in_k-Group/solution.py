from typing import Optional
from common.list_node import ListNode

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        p = dummy
        stack = []
        while True:
            n = k
            tmp = p.next
            while tmp and n:
                stack.append(tmp)
                tmp = tmp.next
                n -= 1
            if n:
                p.next = tmp
                break
            while stack:
                p.next = stack.pop()
                p = p.next
            p.next = tmp
        return dummy.next

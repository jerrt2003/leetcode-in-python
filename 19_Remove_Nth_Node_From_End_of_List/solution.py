from common.list_node import ListNode

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head

        p, q = dummy, dummy
        # q 先走 n+1 步，然后 p 和 q 一起走，直到 q 走到最后一个节点
        # 这样 p 就是倒数第 n+1 个节点
        # 然后 p.next = p.next.next 就可以删除倒数第 n 个节点
        for _ in range(n+1):
            q = q.next

        while q:
            p = p.next
            q = q.next

        p.next = p.next.next

        return dummy.next

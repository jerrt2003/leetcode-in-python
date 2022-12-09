from typing import Optional

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def deleteDuplicates(self, head: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        prev = dummy
        curr = head
        while curr:
            # 跳过当前的重复节点，使得cur指向当前重复元素的最后一个位置
            while curr.next and curr.val == curr.next.val:
                curr = curr.next
            # pre和cur之间没有重复节点，pre后移
            if prev.next == curr:
                prev = prev.next
            # pre->next指向cur的下一个位置（相当于跳过了当前的重复元素）
            # 但是pre不移动，仍然指向已经遍历的链表结尾                
            else:
                prev.next = curr.next
            curr = curr.next
        return dummy.next
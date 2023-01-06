from typing import List, Optional, Tuple

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        # init ans
        ans: List[int] = []
        # init stack, stack為一個monotone stack 單調棧
        # 其儲存數據結構為一個pair: ListNode 和 idx (ListNode也可以改為ListNode的val)
        # ListNode: 就是該ListNode, 用來比較大小使用
        # idx: 對應該ListNode在ans中的idx, 當該pair入棧時我們無法確定下一個大於該node
        # 的數為何,所以先暫存idx以便稍後使用
        stack: List[Tuple[ListNode, int]] = []

        # init idx as 0
        idx = 0
        # go through linkedlist
        while head:
            # 當棧不為空且當前node(node_A)大於棧最上層node(node_B)的val時 
            # 代表node_A val為下一個大於node_B的val (i.e. node_B的答案)
            # 所以node_B出棧然後根據其idx去update 'ans'的值
            while stack and head.val > stack[-1][0].val:
                _, prev_idx = stack.pop()
                ans[prev_idx] = head.val
            stack.append((head, idx))
            ans.append(0)
            idx += 1
            head = head.next

        # return ans
        return ans
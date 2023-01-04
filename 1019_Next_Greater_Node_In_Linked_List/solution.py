from typing import List, Optional, Tuple

# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def nextLargerNodes(self, head: Optional[ListNode]) -> List[int]:
        # init ans and stack
        ans: List[int] = []
        stack: List[Tuple[ListNode, int]] = []

        # go through the linked list 
        idx = 0
        while head:
            # while curr node's val > stack[-1], then pop the stack and 
            # fill in the 'ans' with curr node's val till val < stack[-1]                
            while stack and head.val > stack[-1][0].val:
                _, prev_idx = stack.pop()
                ans[prev_idx] = head.val
            stack.append((head, idx))
            ans.append(0)
            idx += 1
            head = head.next

        # return ans
        return ans
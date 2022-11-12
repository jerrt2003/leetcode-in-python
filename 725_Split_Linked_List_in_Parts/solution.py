# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        cnt = 0
        root_cnt = root
        while root_cnt:
            root_cnt = root_cnt.next
            cnt += 1

        arr = [cnt/k] * k
        rem = cnt % k

        i = 0
        while rem > 0:
            arr[i] += 1
            rem -= 1
            i += 1

        ans = []
        for cnt in arr:
            if cnt == 0:
                ans.append(None)
            else:
                head = curr = root
                for _ in range(cnt-1):
                    curr = curr.next
                root = curr.next
                curr.next = None
                ans.append(head)

        return ans
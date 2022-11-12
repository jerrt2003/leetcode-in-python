# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sortedListToBST(self, head):
        """
        Facebook
        DFS + List
        T:O(n) S:O(n)
        Runtime: 132 ms, faster than 60.63% of Python online submissions for Convert Sorted List to Binary Search Tree.
        Memory Usage: 24.9 MB, less than 35.29% of Python online submissions for Convert Sorted List to Binary Search Tree.
        :type head: ListNode
        :rtype: TreeNode
        """

        def dfs(nodes):
            if len(nodes) == 0:
                return None
            elif len(nodes) == 1:
                return TreeNode(val=nodes[0].val)
            else:
                m = len(nodes) / 2
                node = TreeNode(val=nodes[m].val)
                node.left = dfs(nodes[0:m])
                node.right = dfs(nodes[m + 1:])
                return node

        nodes = []
        while head:
            nodes.append(head)
            head = head.next

        return dfs(nodes)
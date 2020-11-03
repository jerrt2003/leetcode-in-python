# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
import collections
import heapq


class Solution(object):
    def verticalTraversal(self, root):
        """
        T:O(nlog(n)) S:O(n)
        Runtime: 12 ms, faster than 98.70% of Python online submissions for Vertical Order Traversal of a Binary Tree.
        Memory Usage: 13 MB, less than 65.79% of Python online submissions for Vertical Order Traversal of a Binary Tree.
        :type root: TreeNode
        :rtype: List[List[int]]
        """
        graph = collections.defaultdict(list)
        queue = []
        heapq.heappush(queue, (root.val, root, 0))
        while len(queue) != 0:
            new_queue = []
            for i in range(len(queue)):
                node_val, node, col_idx = heapq.heappop(queue)
                graph[col_idx].append(node_val)
                if node.left:
                    heapq.heappush(new_queue, (node.left.val, node.left, col_idx-1))
                if node.right:
                    heapq.heappush(new_queue, (node.right.val, node.right, col_idx+1))
            queue = new_queue

        ans = []
        for idx in sorted(graph.keys()):
            ans.append(graph[idx])
        return ans
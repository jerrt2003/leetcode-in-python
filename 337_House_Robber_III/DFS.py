# -*- coding: utf-8 -*-
# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def rob(self, root):
        """
        Solution: DFS + DP
        Time Complexity:
        Space Complexity:
        TP:
        - For each node we have 2 choice: to rob it or not to rob it
            - if we decide to rob this node, than we can't rob its child node, instead we can only its grand-child node
            - if we decide not to rob this node, then we can rob its child node
        - In order to save time, we can use DP
            - create a dict to store {node: its_max_value}
        :type root: TreeNode
        :rtype: int
        """
        self.max_dict = dict()
        return self.dfs(root)

    def dfs(self, node):
        if node in self.max_dict: return self.max_dict[node]
        if node is None:
            return 0
        if node.left is None and node.right is None: # if current node is leaf node, just return its value
            return node.val
        # every level we have 2 options: rob or not rob
        rob_current_node = node.val
        if node.left is not None:
            rob_current_node = rob_current_node + self.dfs(node.left.left) + self.dfs(node.left.right)
        if node.right is not None:
            rob_current_node = rob_current_node + self.dfs(node.right.left) + self.dfs(node.right.right)
        not_rob_current_node = self.dfs(node.left) + self.dfs(node.right)
        val = max(rob_current_node, not_rob_current_node)
        self.max_dict[node] = val
        return val

N1 = TreeNode(3)
N2 = TreeNode(4)
N3 = TreeNode(5)
N4 = TreeNode(1)
N5 = TreeNode(3)
N6 = TreeNode(1)
N1.left = N2
N1.right = N3
N2.left = N4
N2.right = N5
N3.right = N6

'''
N1 = TreeNode(4)
N2 = TreeNode(1)
N3 = TreeNode(2)
N4 = TreeNode(3)
N1.left = N2
N2.left = N3
N3.left = N4
'''

sol = Solution()
print sol.rob(N1)
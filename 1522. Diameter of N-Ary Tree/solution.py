"""
# Definition for a Node.
class Node(object):
    def __init__(self, val=None, children=None):
        self.val = val
        self.children = children if children is not None else []
"""


class Solution(object):
    def diameter(self, root):
        """
        Facebook
        T:O(nlog(n)) S:O(n)
        Runtime: 44 ms, faster than 80.49% of Python online submissions for Diameter of N-Ary Tree.
        Memory Usage: 15.9 MB, less than 41.67% of Python online submissions for Diameter of N-Ary Tree.
        :type root: 'Node'
        :rtype: int
        """
        self.ans = 0

        def dfs(node):
            if not node.children:
                return 1
            candidate = [dfs(n) for n in node.children]
            candidate.sort(reverse=True)
            if len(candidate) < 2:
                self.ans = max(self.ans, candidate[0])
            else:
                self.ans = max(self.ans, candidate[0] + candidate[1])
            return 1 + candidate[0]

        dfs(root)
        return self.ans
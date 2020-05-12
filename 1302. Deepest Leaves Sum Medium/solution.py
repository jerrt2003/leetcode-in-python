# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deepestLeavesSum(self, root):
        """
        T:O(n) S:O(n)
        Runtime: 100 ms, faster than 55.90% of Python online submissions for Deepest Leaves Sum.
        Memory Usage: 20.2 MB, less than 100.00% of Python online submissions for Deepest Leaves Sum.
        :type root: TreeNode
        :rtype: int
        """
    #     self.levelSum = []
    #     self.dfs(root, 1)
    #     return self.levelSum[-1]
    #
    # def dfs(self, node, lv):
    #     if not node:
    #         return
    #     if lv > len(self.levelSum):
    #         self.levelSum.append(node.val)
    #     else:
    #         self.levelSum[lv-1] += node.val
    #     self.dfs(node.left, lv+1)
    #     self.dfs(node.right, lv+1)


        """
        BFS: T:O(n) S:O(n)
        Runtime: 104 ms, faster than 44.88% of Python online submissions for Deepest Leaves Sum.
        Memory Usage: 20.5 MB, less than 100.00% of Python online submissions for Deepest Leaves Sum.
        """
        res = []
        stack = [(root, 0)]
        while stack:
            node, lv = stack.pop(0)
            if len(res) < lv+1:
                res.append(0)
            res[lv] += node.val
            if node.left:
                stack.append((node.left, lv+1))
            if node.right:
                stack.append((node.right, lv+1))
        return res[-1]
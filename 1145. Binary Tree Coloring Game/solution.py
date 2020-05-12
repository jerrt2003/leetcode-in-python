# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    # def btreeGameWinningMove(self, root, n, x):
    #     """
    #     BFS
    #     T:O(n) S:O(1)
    #     Runtime: 24 ms, faster than 38.00% of Python online submissions for Binary Tree Coloring Game.
    #     Memory Usage: 13 MB, less than 100.00% of Python online submissions for Binary Tree Coloring Game.
    #     :type root: TreeNode
    #     :type n: int
    #     :type x: int
    #     :rtype: bool
    #     """
    #     # 3 zones: zone1 -> above x node, zone 2 -> x node left tree, zone 3 -> x node right tree
    #     queue = [root]
    #     z1Count = 0
    #     redNode = None
    #     while queue:
    #         curr = queue.pop(0)
    #         if curr.val != x:
    #             z1Count += 1
    #             if curr.left:
    #                 queue.append(curr.left)
    #             if curr.right:
    #                 queue.append(curr.right)
    #         else:
    #             redNode = curr
    #     z2Count = 0
    #     if redNode.left:
    #         queue.append(redNode.left)
    #         while queue:
    #             curr = queue.pop(0)
    #             z2Count += 1
    #             if curr.left:
    #                 queue.append(curr.left)
    #             if curr.right:
    #                 queue.append(curr.right)
    #     z3Count = n-1-z1Count-z2Count
    #     rank = sorted([z1Count, z2Count, z3Count])
    #     if rank[2] > rank[0]+rank[1]+1:
    #         return True
    #     else:
    #         return False
    def btreeGameWinningMove(self, root, n, x):
        """
        DFS
        T:O(n) S:O(1)
        Runtime: 20 ms, faster than 72.00% of Python online submissions for Binary Tree Coloring Game.
        Memory Usage: 12.7 MB, less than 100.00% of Python online submissions for Binary Tree Coloring Game.
        :type root: TreeNode
        :type n: int
        :type x: int
        :rtype: bool
        """
        # redLeftCount = 0
        # redRightCount = 0
        c = [0, 0]

        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            if root.val == x:
                c[0] = left
                c[1] = right
            return 1+left+right

        return dfs(root)/2 < max(max(c), n-sum(c)-1)





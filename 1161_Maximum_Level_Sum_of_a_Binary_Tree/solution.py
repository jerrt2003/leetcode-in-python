# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxLevelSum(self, root):
        """
        BFS
        T:O(n) S:O(n)
        Runtime: 352 ms, faster than 69.12% of Python online submissions for Maximum Level Sum of a Binary Tree.
        Memory Usage: 21.1 MB, less than 100.00% of Python online submissions for Maximum Level Sum of a Binary Tree.
        (optimize version)
        Runtime: 328 ms, faster than 92.92% of Python online submissions for Maximum Level Sum of a Binary Tree.
        Memory Usage: 20.9 MB, less than 100.00% of Python online submissions for Maximum Level Sum of a Binary Tree.
        :type root: TreeNode
        :rtype: int
        """
        # maxSum = -float('inf')
        # ret, level = 0, 0
        # queue = [root]
        # while queue:
        #     levelSum = 0
        #     level += 1
        #     for i in range(len(queue)):
        #         node = queue.pop(0)
        #         levelSum += node.val
        #         if node.left:
        #             queue.append(node.left)
        #         if node.right:
        #             queue.append(node.right)
        #     if levelSum > maxSum:
        #         maxSum = levelSum
        #         ret = level
        #     else:
        #         continue
        # return ret
        maxSum = -float('inf')
        currLevel = maxLevel = 0
        queue = [root]
        while queue:
            currLevel += 1
            currSum = sum([node.val for node in queue])
            if currSum > maxSum:
                maxSum = currSum
                maxLevel = currLevel
            queue = [y for node in queue for y in [node.left, node.right] if y]
        return maxLevel
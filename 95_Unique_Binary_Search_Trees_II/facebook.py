# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def generateTrees(self, n):
        """
        Facebook
        T:O(nCn) S:O(nCn) --> Cn: Catalan number
        Runtime: 52 ms, faster than 75.63% of Python online submissions for Unique Binary Search Trees II.
        Memory Usage: 15.8 MB, less than 76.54% of Python online submissions for Unique Binary Search Trees II.
        :type n: int
        :rtype: List[TreeNode]
        """

        def dfs(node_list):
            if not node_list:
                return [None]
            ret_list = []
            for i, v in enumerate(node_list):
                left_node_list = dfs(node_list[:i])
                right_node_list = dfs(node_list[i + 1:])
                for left in left_node_list:
                    for right in right_node_list:
                        node = TreeNode(v)
                        node.left = left
                        node.right = right
                        ret_list.append(node)
            return ret_list

        return dfs(range(1,n+1))

print Solution().generateTrees(3)
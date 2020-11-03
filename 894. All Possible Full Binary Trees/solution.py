# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    DP = {0:[], 1:[TreeNode(0)]}

    def allPossibleFBT(self, N):
        """
        Tree
        Recursion + Memo
        T:O(n) S:O(n)
        Runtime: 180 ms, faster than 94.29% of Python online submissions for All Possible Full Binary Trees.
        Memory Usage: 16.4 MB, less than 95.35% of Python online submissions for All Possible Full Binary Trees.
        :type N: int
        :rtype: List[TreeNode]
        """
        if N not in Solution.DP:
            if N % 2 == 0:
                return []
            if N == 1:
                return [TreeNode(0)]
            res = []
            for L in range(1, N, 2):
                R = N-1-L
                l_root_list = self.allPossibleFBT(L)
                r_root_list = self.allPossibleFBT(R)
                for l_root in l_root_list:
                    for r_root in r_root_list:
                        root = TreeNode(0)
                        root.left = l_root
                        root.right = r_root
                        res.append(root)
            Solution.DP[N] = res
        return Solution.DP[N]

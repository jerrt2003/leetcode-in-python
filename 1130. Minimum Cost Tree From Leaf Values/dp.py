class Solution(object):
    def mctFromLeafValues(self, arr):
        """
        DP
        T:O(n^3) S:O(n^2)
        Runtime: 344 ms, faster than 6.36% of Python online submissions for Minimum Cost Tree From Leaf Values.
        Memory Usage: 13.2 MB, less than 6.99% of Python online submissions for Minimum Cost Tree From Leaf Values.
        https://leetcode.com/problems/minimum-cost-tree-from-leaf-values/discuss/340004/Python-Easy-DP
        :type arr: List[int]
        :rtype: int
        """
        self.cache = dict()
        def dp(i, j):
            if i == j:
                return 0
            if (i, j) in self.cache:
                return self.cache[(i, j)]
            self.cache[(i, j)] = float('inf')
            for k in range(i+1, j+1):
                self.cache[(i, j)] = min(self.cache[(i, j)], dp(i, k-1)+dp(k, j)+max(arr[i:k])*max(arr[k:j+1]))
            return self.cache[(i, j)]

        return dp(0, len(arr)-1)

print Solution().mctFromLeafValues([6,2,4])
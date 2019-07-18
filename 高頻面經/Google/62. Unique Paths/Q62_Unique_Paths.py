class Solution(object):
    def uniquePaths(self, m, n):
        """
        DP Solution.
        Visualize: leetcode.com/problems/unique-paths/discuss/22953/Java-DP-solution-with-complexity-O(n*m)/22355
        Time complexity: O(m*n)
        Space complexity: O(m*n)
        :type m: int
        :type n: int
        :rtype: int
        """
        path = [[0]*n] * m
        for i in range(m):
            path[i][0] = 1
        for j in range(n):
            path[0][j] = 1
        for i in range(1,m):
            for j in range(1,n):
                path[i][j] = path[i-1][j] + path[i][j-1]
        return path[m-1][n-1]




sol = Solution()
print sol.uniquePaths(7, 3)
class Solution(object):
    def countSquares(self, matrix):
        """
        T:O(m*n) S:O(m*n)
        Runtime: 764 ms, faster than 25.66% of Python online submissions for Count Square Submatrices with All Ones.
        Memory Usage: 14.6 MB, less than 100.00% of Python online submissions for Count Square Submatrices with All Ones.
        :type matrix: List[List[int]]
        :rtype: int
        """
        m, n = len(matrix), len(matrix[0])
        dp = [[0 for _ in range(n+1)] for _ in range(m+1)]
        ans = 0
        for i in range(1, m+1):
            for j in range(1, n+1):
                if matrix[i-1][j-1] == 1:
                    dp[i][j] = min(dp[i-1][j], dp[i][j-1], dp[i-1][j-1]) + 1
                    ans += dp[i][j]

        return ans

class Solution(object):
    def isMatch(self, s, p):
        """
        Facebook
        T:O(m*n) S:O(m*n)
        Runtime: 44 ms, faster than 75.83% of Python online submissions for Regular Expression Matching.
        Memory Usage: 12.9 MB, less than 22.44% of Python online submissions for Regular Expression Matching.
        :type s: str
        :type p: str
        :rtype: bool
        """
        m, n = len(s), len(p)
        DP = [[False for _ in range(n + 1)] for _ in range(m + 1)]
        DP[0][0] = True
        for i in range(1, len(DP[0])):
            pi = i - 1
            if p[pi] == '*':
                DP[0][i] = DP[0][i - 2]

        for i in range(1, m + 1):
            for j in range(1, n + 1):
                si, pi = i - 1, j - 1
                if s[si] == p[pi] or p[pi] == '.':
                    DP[i][j] = DP[i - 1][j - 1]
                elif p[pi] == '*':
                    if DP[i][j - 2]:
                        DP[i][j] = True
                    elif s[si] == p[pi - 1] or p[pi - 1] == '.':
                        DP[i][j] = DP[i - 1][j]

        return DP[-1][-1]
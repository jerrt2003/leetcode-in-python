class Solution(object):
    def findMatch(self, S, P):
        m, n = len(S), len(P)
        DP = [[False for _ in range(n+1)] for _ in range(m+1)]
        DP[0][0] = True
        for i in range(1, m+1):
            for j in range(1, n+1):
                Si, Pi = i-1, j-1
                if S[Si] == P[Pi] or P[Pi] == '.':
                    DP[i][j] = DP[i-1][j-1]

        return DP[-1][-1]

print Solution().findMatch('ADBECF','A.B.C.')
print Solution().findMatch('ADBEC','A.B.C.')
# DP
class Solution:
    def countSubstrings(self, s: str) -> int:
        m = len(s)
        DP = [[False for _ in range(m)] for _ in range(m)]
        ans = 0

        for i in range(m):
            DP[i][i] = True
            ans += 1

        for r in range(1, m):
            for l in range(r):
                if s[l] == s[r] and (DP[l + 1][r - 1] or r - l + 1 <= 2):
                    DP[l][r] = True
                    ans += 1

        return ans

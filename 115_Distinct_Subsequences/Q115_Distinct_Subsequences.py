class Solution(object):
    def numDistinct(self, s, t):
        """
        DP Solution
        Time Complexity: O(n^2)
        Space Complexity: O(mn)
        Inspired by: https://leetcode.com/problems/distinct-subsequences/discuss/37387/A-DP-solution-with-clarification-and-explanation
        :type s: str
        :type t: str
        :rtype: int
        """
        # Create a DP 2-D array: s_len+1 x t_len+1
        # Why needs +1..?
        # DP[i][0] stands for S is empty string, there is no sub-sequence in S will match T
        s_len = len(s)
        t_len = len(t)
        DP = [[0 for _ in range(s_len+1)] for _ in range(t_len+1)]
        # DP[0][j] stands for T is empty string, the sub-sequence of for S from idx 0 to idx j to
        # T is 1 (to delete every char in S[idx_0...idx_j]
        for j in range(s_len+1):
            DP[0][j] = 1
        # DP[i][j] stands for sub-sequence count in S[0..j] for T[0..i]
        for i in range(1,t_len+1): # start with 1 since 0 is already used to represent empty string T
            for j in range(1,s_len+1): # start with 1 since 0 is already used to represent empty string S
                # if t[i-1] != s[j-1] means char s[j-1] will not form a valid sub-sequence string of t[i-1]
                if t[i-1] != s[j-1]: # To subtract 1 since python string idx starts from 0
                    # thus DP[i][j] will be DP[i][j-1] (no adding)
                    DP[i][j] = DP[i][j-1]
                elif t[i-1] == s[j-1]:
                    #  if T[i] == S[j], then first we could adopt the solution in case 1),
                    # but also we could match the characters T[i] and S[j] and align the rest of them (i.e. T[0..(i-1)]
                    # and S[0..(j-1)]. As a result, dp[i][j] = dp[i][j-1] + d[i-1][j-1]
                    DP[i][j] = DP[i][j-1] + DP[i-1][j-1]
        return DP[t_len][s_len]



S = 'babgbag'
T = 'bag'

sol = Solution()
print sol.numDistinct(S,T)
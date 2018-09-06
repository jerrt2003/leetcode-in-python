class Solution(object):
    def minDistance(self, word1, word2):
        """
        DP Solution
        Explanation: https://leetcode.com/problems/edit-distance/discuss/25846/20ms-Detailed-Explained-C++-Solutions-(O(n)-Space)
        Time Complexity: O(n*m)
        Space Complexity: O(n+m)
        :type word1: str
        :type word2: str
        :rtype: int
        """
        m = len(word1)
        n = len(word2)
        # Can't use [[0]*(n+1)]*(m+1) since will duplicates
        DP = [[0 for x in range(n+1)] for y in range(m+1)]
        for i in range(1,m+1):
            DP[i][0] = i
        for j in range(1, n+1):
            DP[0][j] = j
        for i in range(1, m+1):
            for j in range(1, n+1):
                if word1[i-1] == word2[j-1]:
                    DP[i][j] = DP[i-1][j-1]
                else:
                    DP[i][j] = min(DP[i-1][j], DP[i][j-1], DP[i-1][j-1]) + 1
        return DP[m][n]

word1 = 'horse'
word2 = 'ros'

sol = Solution()
print sol.minDistance(word1,word2)
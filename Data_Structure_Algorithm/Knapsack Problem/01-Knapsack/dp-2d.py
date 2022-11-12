class Solution(object):
    def knapsack(self, w, v, W):
        """
        DP[i][j] = max(DP[i-1][j],DP[i-1][j-w[i]]+v[i])
        :type arr: List[int]
        :rtype: int
        """
        m, n = len(w), W
        DP = [[0 for _ in range(W+1)] for _ in range(m+1)]
        for i in range(1, m+1):
            tmp = DP[:]
            for j in range(w[i-1], W+1):
                tmp[i][j] = max(DP[i-1][j], DP[i-1][j-w[i-1]]+v[i-1]) # w[i-1], v[i-1] --> need to offset by 1
            DP = tmp
        return DP[-1][-1]




print Solution().knapsack([10,20,30],[60,100,120],50)
print Solution().knapsack([1,1,2,2],[1,2,4,5],4)
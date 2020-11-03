class Solution(object):
    def lastStoneWeightII(self, stones):
        """
        T:O(mn) S:O(n)
        Runtime: 0 ms, faster than 100.00% of Go online submissions for Last Stone Weight II.
        Memory Usage: 2.1 MB, less than 77.27% of Go online submissions for Last Stone Weight II.
        :type stones: List[int]
        :rtype: int
        """
        W = sum(stones)
        DP = [0 for _ in range(W/2+1)]
        for i in range(1, len(stones)+1):
            for j in range(W/2, stones[i-1]-1, -1):
                DP[j] = max(DP[j], DP[j-stones[i-1]]+stones[i-1])
        return W - 2*DP[-1]



print Solution().lastStoneWeightII([2,7,4,1,8,1])
class Solution(object):
    def maxSideLength(self, mat, threshold):
        """
        :type mat: List[List[int]]
        :type threshold: int
        :rtype: int
        """
        # build prefix
        # prefixSum = [[0 for j in range(len(mat[0])+1)] for i in range(len(mat)+1)]
        # for i in range(1, len(prefixSum)):
        #     for j in range(1, len(prefixSum[0])):
        #         prefixSum[i][j] = prefixSum[i-1][j]+prefixSum[i][j-1]-prefixSum[i-1][j-1]+mat[i-1][j-1]
        m, n = len(mat[0]), len(mat)

        # build pre_sum
        prefixSum = [[0 for j in range(m + 1)] for i in range(n + 1)]
        for i in range(1, n + 1):
            for j in range(1, m + 1):
                prefixSum[i][j] = prefixSum[i - 1][j] + prefixSum[i][j - 1] - prefixSum[i - 1][j - 1] + mat[i - 1][j - 1]

        def isValid(k):
            for i in range(1, len(prefixSum)-k):
                for j in range(1, len(prefixSum[0])-k):
                    curSum = prefixSum[i+k][j+k]-prefixSum[i-1][j+k]-prefixSum[i+k][j-1]+prefixSum[i-1][j-1]
                    if curSum <= threshold:
                        return True
            return False

        l, r = 0, min(len(mat), len(mat[0]))+1
        while l < r:
            m = (l+r-1)/2
            if not isValid(m):
                r = m
            else:
                l = m+1
        return 0 if l == 0 else l-1

# print Solution().maxSideLength([[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]], 4)
# print Solution().maxSideLength([[1,1,1,1],[1,0,0,0],[1,0,0,0],[1,0,0,0]], 6)
print Solution().maxSideLength([[18,70],[61,1],[25,85],[14,40],[11,96],[97,96],[63,45]], 40184)
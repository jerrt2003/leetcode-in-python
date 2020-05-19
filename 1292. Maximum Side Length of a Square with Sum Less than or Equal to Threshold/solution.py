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
        m, n = len(mat), len(mat[0])
        p = [[0 for _ in range(n+1)] for _ in range(m+1)]
        for i in range(1, m+1):
            for j in range(1, n+1):
                p[i][j] = p[i-1][j]+p[i][j-1]-p[i-1][j-1]+mat[i-1][j-1]

        def isValid(k):
            for i in range(m-k):
                for j in range(n-k):
                    sq_sum = p[i+k][j+k]-p[i][j+k]-p[i+k][j]+p[i][j]
                    if sq_sum <= threshold:
                        return True
            return False

        l, r = 0, min(m, n)+1
        while l < r:
            mid = (l+r-1)//2
            if not isValid(mid):
                r = mid
            else:
                l = mid+1
        return 0 if l == 0 else l-1


print(Solution().maxSideLength([[1,1,3,2,4,3,2],[1,1,3,2,4,3,2],[1,1,3,2,4,3,2]],4))
print(Solution().maxSideLength([[1,1,0],[1,1,1],[1,0,1]],4))
print(Solution().maxSideLength([[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2],[2,2,2,2,2]],1))
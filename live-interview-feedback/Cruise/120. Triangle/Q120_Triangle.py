class Solution(object):
    def minimumTotal(self, triangle):
        """
        DP: Bottom-Up Solution
        :type triangle: List[List[int]]
        :rtype: int
        """
        DP = triangle[-1] # First DP is the last row in triangle
        len_triangle = len(triangle)
        for i in range(len_triangle-2,-1,-1): # 從倒數第二列開始算, 因為要算到第0列,所以上限為-1
            for idx in range(0, len(triangle[i])):
                # DP[i]會是前一組DP[i]與DP[i+1]的最小值+自己triangle[i][idx]
                # 此處可以直接把DP[idx]替換掉是因為下一個loop不會用到
                DP[idx] = min(DP[idx],DP[idx+1]) + triangle[i][idx]
        return DP[0]

#'''
triangle = [
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]
#'''

#triangle = [[-1],[2,3],[1,-1,-3]]

sol = Solution()
print sol.minimumTotal(triangle)
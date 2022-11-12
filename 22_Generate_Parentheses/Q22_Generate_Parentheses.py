class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ans = []
        def findParenthesis(comb = '', i=0, j=0):
            if len(comb) == 2*n:
                ans.append(comb)
                return
            if i < n:
                findParenthesis(comb+'(', i+1, j)
            if j < i:
                findParenthesis(comb+')', i, j+1)

        findParenthesis()
        return ans


x = 3
sol = Solution()
print sol.generateParenthesis(x)
class Solution(object):
    def countNumbersWithUniqueDigits(self, n):
        """
        :time complexity: O(n)
        :space complexity: O(n)
        :type n: int
        :rtype: int
        """
        if n is None or not isinstance(n, int):
            return None
        DP = dict()
        DP[0] = 1
        DP[1] = 9
        if n == 0: return DP[0]
        if n == 1: return DP[1]+DP[0]
        if n > 10: n = 10
        result = 0
        for i in range(n+1):
            if i == 0 or i == 1:
                continue
            DP[i] = DP[i-1]*(10-i+1)
            result += DP[i]
        return result + DP[1] + DP[0]

sol = Solution()
n = 1
print sol.countNumbersWithUniqueDigits(n)
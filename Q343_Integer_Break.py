class Solution(object):
    '''
    My recursive solution ==> WRONG !!
    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 2: return 1
        if n == 3: return 2
        self.result = list()
        self._integerBreak(n)
        tmp = 1
        for i in self.result:
            tmp *= i
        return tmp

    def _integerBreak(self, n):
        if n/2 == 1 or n/2 == 0:
            self.result.append(n)
        elif n%2 == 0:
            a = b = n/2
            self._integerBreak(a)
            self._integerBreak(b)
        else:
            a = n/2
            b = n/2 + 1
            self._integerBreak(a)
            self._integerBreak(b)
        return
    '''

    def integerBreak(self, n):
        """
        :type n: int
        :rtype: int
        """
        if n == 0: return 0
        if n <= 2: return 1
        if n == 3: return 2
        if n == 4: return 4
        DP = dict()
        DP[2] = 2
        DP[3] = 3
        DP[4] = 4
        for i in range(5, n+1):
            DP[i] = 3*DP[i-3]
        return DP[n]
    



input = 10
sol = Solution()
print sol.integerBreak(input)

import math
class Solution(object):
    '''
    def knightProbability(self, N, K, r, c):
        """
        Recursion Method
        :type N: int
        :type K: int
        :type r: int
        :type c: int
        :rtype: float
        """
        self.res = 0
        self.const = K
        self._knightProbability(N, K, r, c)
        return self.res

    def _knightProbability(self, N, K, r, c):
        if (0 <= r < N) and (0 <= c < N) and K == 0:
            self.res += math.pow(0.125, self.const)
        elif (r < 0 or r > N-1) or (c < 0 or c > N-1):
                return
        else:
            self._knightProbability(N, K - 1, r - 2, c - 1)
            self._knightProbability(N, K - 1, r - 2, c + 1)
            self._knightProbability(N, K - 1, r - 1, c - 2)
            self._knightProbability(N, K - 1, r - 1, c + 2)
            self._knightProbability(N, K - 1, r + 2, c - 1)
            self._knightProbability(N, K - 1, r + 2, c + 1)
            self._knightProbability(N, K - 1, r + 1, c - 2)
            self._knightProbability(N, K - 1, r + 1, c + 2)
    '''

    def knightProbability(self, N, K, r, c):
        """
        DP Method: derive from recursive
        Using dict as memorization: TLE
        Using try/catch: beat 4.76%
        :type N: int
        :type K: int
        :type r: int
        :type c: int
        :rtype: float
        """
        self.moves = [
            (-2, -1),
            (-2, +1),
            (-1, -2),
            (-1, +2),
            (+2, -1),
            (+2, +1),
            (+1, -2),
            (+1, +2)
        ]
        self.DP = dict()
        return self._knightProbability(N, K, r, c)

    def _knightProbability(self, N, K, r, c):
        if r < 0 or r > N-1 or c < 0 or c > N-1: # over chase board
            return 0
        if K == 0:
            return 1
        if (r, c, K) in self.DP.keys():
            return self.DP[(r, c, K)]
        rate = 0
        for row_move, column_move in self.moves:
            # means at location r, c with K move, the total possibility not move out of bound
            rate += 0.125*self._knightProbability(N, K-1, r+row_move, c+column_move)
        self.DP[(r, c, K)] = rate
        return rate




sol = Solution()
print sol.knightProbability(3, 3, 0, 0)
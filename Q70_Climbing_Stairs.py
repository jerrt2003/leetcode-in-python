class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """
        #return self.climb_stairs_recursive(0, n)
        self.combination = dict()
        for i in range(n):
            self.combination[i] = None
        #return self.climb_stair_memorization(0, n)
        return self.climb_stair_DP(n)

    def climb_stairs_recursive(self, current_stair, total_stair):
        """
        A recursive solution to find all combination
        :param current_stair:
        :param total_stair:
        :return:
        """
        if current_stair == total_stair:
            return 1
        elif current_stair > total_stair:
            return 0
        else:
            return self.climb_stairs_recursive(current_stair+1, total_stair) + self.climb_stairs_recursive(current_stair+2, total_stair)

    def climb_stair_memorization(self, current_stair, total_stair):
        """
        Top-to-bottom approach
        :param current_stair:
        :param total_stair:
        :return:
        """
        if current_stair == total_stair:
            return 1
        elif current_stair > total_stair:
            return 0
        else:
            if self.combination[current_stair] is not None:
                return self.combination[current_stair]
            else:
                tmp = self.climb_stair_memorization(current_stair+1, total_stair) + self.climb_stair_memorization(current_stair+2, total_stair)
                self.combination[current_stair] = tmp
                return tmp

    def climb_stair_DP(self, n):
        """
        DP[n] = DP[n-1] + DP[n-2]
        :param n:
        :return:
        """
        if n == 0: return 0
        if n == 1: return 1
        self.combination[1] = 1
        self.combination[2] = 2
        for i in range(3, n+1):
            self.combination[i] = self.combination[i-1] + self.combination[i-2]
        return self.combination[n]


num_stair = 10
sol = Solution()
print sol.climbStairs(num_stair)
# -*- coding: utf-8 -*-
class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        l = len(M)
        count = 0

        def findFriend(i, j):
            if M[i][j] <= 0: return False
            M[i][j] = -1
            if i > 0:
                findFriend(i-1, j)
            if i < l-1:
                findFriend(i+1, j)
            if j > 0:
                findFriend(i, j-1)
            if j < l-1:
                findFriend(i, j+1)
            return True

        for i in range(l):
            for j in range(l):
                if findFriend(i, j):
                    count += 1
        return count

M = [[1,0,0,1],
     [0,1,1,0],
     [0,1,1,1],
     [1,0,1,1]]


sol = Solution()
print sol.findCircleNum(M)
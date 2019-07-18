# -*- coding: utf-8 -*-
class Solution(object):
    def optimalSolution(self, cards):
        m = len(cards)
        DP = [[0 for _ in range(m)] for _ in range(m)]
        for l in range(m):
            for i in range(m-l):
                j = i + l
                if i == j:
                    DP[i][j] = cards[i]
                elif j == i+1:
                    DP[i][j] = max(cards[i],cards[j])
                else:
                    DP[i][j] = max(cards[i]+min(DP[i+1][j-1],DP[i+2][j]), cards[j]+min(DP[i][j-2],DP[i+1][j-1]))
        return DP[0][m-1]

arr1 = [8,15,3,7]
assert Solution().optimalSolution(arr1) == 22

arr2 = [2,2,2,2]
assert Solution().optimalSolution(arr2) == 4

arr3 = [ 20, 30, 2, 2, 2, 10]
assert Solution().optimalSolution(arr3) == 42
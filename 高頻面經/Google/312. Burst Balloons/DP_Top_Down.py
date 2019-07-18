# -*- coding: utf-8 -*-
class Solution(object):
    def maxCoins(self, nums):
        """
        DP: Top-Down
        Time Complexity:
        Space Complexity:
        Inspired by: https://leetcode.com/problems/burst-balloons/discuss/76243/Python-DP-N3-Solutions
        Algorithm:
        - Key thoughts: divide and conquer !!
        - Create a 2-D DP array to store maximum value: DP = [[0 for _ in range(len(nums)+1)] for _ in range(len(nums)+1)]
        - DP[i][j] means maximum burst balloon value between index i and j
        - DP[i][j] = max(DP[i][j], nums[i]*nums[k]*nums[j] + DP[i][k] + DP[k][j])
        - WHY nums[i]*nums[k]*nums[j] + DP[i][k] + DP[k][j] => since we are assuming k is the last balloon to burst
        (e.g. i, k, j is the last 3 balloons left) (leetcode.com/problems/burst-balloons/discuss/76243/Python-DP-N3-Solutions/79828)
        - if DP[i][j] is not 0 or j == i+1: return DP[i][j] WHY..?
        cuz DP[i][j] = max(DP[i][j], nums[i]*nums[k]*nums[j] + DP[i][k] + DP[k][j]), since no middle k (e.g. k is 0)
        so we just need to return DP[i][j]
        :type nums: List[int]
        :rtype: int
        """
        nums = [1] + nums + [1]
        len_nums = len(nums)
        DP = [[0 for _ in range(len_nums)] for _ in range(len_nums)]
        def findMaxCoins(i, j):
            if DP[i][j] != 0 or j == i+1: # 若是j == i+1即代表中間k=0所以return DP[i][j]即可
                return DP[i][j]
            coins = 0
            for k in range(i+1, j):
                # 在此findMaxCoins(i,k)代表的是說往前找, 找到最極限後在慢慢加回來(類似recursion),所以是所謂的Top-Down
                coins = max(coins, nums[i]*nums[k]*nums[j] + findMaxCoins(i,k) + findMaxCoins(k,j))
            DP[i][j] = coins
            return coins

        return findMaxCoins(0, len_nums-1)

nums = [3,1,5,8]
sol = Solution()
print sol.maxCoins(nums)

# -*- coding: utf-8 -*-
class Solution(object):
    def maxCoins(self, nums):
        """
        Solution: DP Bottom-Up
        Time Complexity:
        Space Complexity:
        Inspired by: https://leetcode.com/problems/burst-balloons/discuss/76243/Python-DP-N3-Solutions
        https://leetcode.com/problems/burst-balloons/discuss/76228/Share-some-analysis-and-explanations
        Algorithm:
        - Key thoughts: divide and conquer !!
        - Create a 2-D DP array to store maximum value: DP = [[0 for _ in range(len(nums))] for _ in range(len(nums))]
        - DP[i][j] means maximum burst balloon value between index i and j (included)
        - DP[i][j] = max(DP[i][j], nums[i]*nums[k]*nums[j] + DP[i][k] + DP[k][j])
        - Unlike Top-Down we'll continue to search our answer based on past result
        - In order to do that we are using range between i, j to help us define the middle point
        so we just need to return DP[i][j]
        :type nums: List[int]
        :rtype: int
        """
        nums = [1] + nums + [1]
        len_nums = len(nums)
        DP = [[0 for _ in range(len_nums)] for _ in range(len_nums)]
        # 最小的gap為2, 最大gap為(len_nums-1)因為不能超出nums的長度
        for gap in range(2, len_nums):
            for left in range(len_nums-gap): # 決定初始left的位置
                right = left + gap # based on left的位置加上gap我們可以得知right的位置
                # 決定中點k的位置
                # 最小為left+1(k !<= left), 最大為right-1(k !>= right)
                for k in range(left+1, right):
                    DP[left][right] = max(DP[left][right], nums[left]*nums[k]*nums[right]+DP[left][k]+DP[k][right])
        return DP[0][len_nums-1]

nums = [3,1,5,8]
sol = Solution()
print sol.maxCoins(nums)
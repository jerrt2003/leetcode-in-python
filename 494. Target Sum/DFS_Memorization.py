# -*- coding: utf-8 -*-
class Solution(object):
    def findTargetSumWays(self, nums, S):
        """
        Solution: DP + Memorization
        Time Complexity:
        Space Complexity:
        Inspired By: https://leetcode.com/problems/target-sum/discuss/97424/Python-intuitive-DFS-solution-with-memorization
        TP:
        - Using DFS and cache information which already being calculated
        - 以idx, curr_result 作為key, 假設這組idx/result已經有result了,我們就可以不用在算
            - 也就是說到達此idx, curr_result的組合不只一種
        :type nums: List[int]
        :type S: inMsg
        :rtype: int
        """
        if nums is None or len(nums) == 0: return 0
        DP = {}
        def findCombo(idx, S):
            if (idx, S) in DP:
                return DP[(idx, S)]
            if idx == len(nums):
                DP[(idx, S)] = 1 if S == 0 else 0
            else:
                DP[(idx, S)] = findCombo(idx+1, S+nums[idx]) + findCombo(idx+1, S-nums[idx])
            return DP[(idx, S)]

        return findCombo(0, S)

nums = [42,24,30,14,38,27,12,29,43,42,5,18,0,1,12,44,45,50,21,47]
S = 38

sol = Solution()
print sol.findTargetSumWays(nums, S)
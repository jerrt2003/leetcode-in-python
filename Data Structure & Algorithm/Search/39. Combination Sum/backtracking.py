# -*- coding: utf-8 -*-
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        Solution: backtracking
        Time Complexity: O(n!)
        Space Complexity:
        Perf: Runtime: 44 ms, faster than 97.82% / Memory Usage: 11.9 MB, less than 5.02%
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []

        def helper(curr_res, curr_idx, target, candidates):
            for i in range(curr_idx, len(candidates)):
                if target - candidates[i] < 0:
                    break
                elif target - candidates[i] == 0:
                    res.append(curr_res + [candidates[i]])
                    break
                else:
                    helper(curr_res+[candidates[i]], i, target - candidates[i], candidates)

        helper([], 0, target, sorted(candidates))
        return res

print Solution().combinationSum([2,3,6,7], 7)
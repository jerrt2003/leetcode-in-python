# -*- coding: utf-8 -*-
class Solution(object):
    def combinationSum2(self, candidates, target):
        """
        Solution: backtracking
        Time Compelxity: O(n!)
        Space Complexity:
        Perf: Runtime: 32 ms, faster than 99.67% / Memory Usage: 11.7 MB, less than 5.16%
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.res = []
        self.helper(0, sorted(candidates), target, [])
        return self.res

    def helper(self, curr_idx, candidates, target, curr_path):
        for i in range(curr_idx, len(candidates)):
            if target < candidates[i]:
                break
            elif target == candidates[i]:
                self.res.append(curr_path + [candidates[i]])
                break
            else:
                if i > curr_idx and candidates[i] == candidates[i-1]:
                    continue
                self.helper(i+1, candidates, target-candidates[i], curr_path+[candidates[i]])

print Solution().combinationSum2([10,1,2,7,6,1,5], 8)
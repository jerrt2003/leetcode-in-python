# -*- coding: utf-8 -*-
class Solution(object):
    def combinationSum(self, candidates, target):
        """
        Solution: Backtracking
        Time Complexity:
        Space Complexity:
        Inspired By: MySELF!! (300ms, 13.79%)
        :type candidates: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        self.res = []
        def helper(curSum, currPath, candidates, target):
            for num in candidates:
                if curSum + num == target:
                    ans = currPath + [num]
                    ans.sort()
                    if ans not in self.res:
                        self.res.append(currPath+[num])
                    break
                elif curSum + num > target:
                    break
                else:
                    helper(curSum+num, currPath+[num], candidates, target)
        candidates.sort()
        for i in range(len(candidates)):
            helper(0, [], candidates[i:], target)
        return self.res

nums = [2,3,6,7]
target = 7
print Solution().combinationSum(nums, target)
# -*- coding: utf-8 -*-
class Solution(object):
    def jump(self, nums):
        """
        Solution: DFS (TLE)
        Time Complexity:
        Space Complexity:
        TP:
        - DFS --> TLE
        :type nums: List[int]
        :rtype: int
        """
        if not nums or nums[0] == 0: return 0
        self.min_jump = float('inf')
        def DFS(idx, jump):
            if idx + nums[idx] >= len(nums)-1:
                self.min_jump = min(jump+1, self.min_jump)
            else:
                for i in range(1, nums[idx]+1):
                    DFS(idx+i, jump+1)
        DFS(0, 0)
        return self.min_jump




#nums = [2,3,1,1,4]
nums = [0]
print Solution().jump(nums)
# -*- coding: utf-8 -*-
class Solution(object):
    def jump(self, nums):
        """
        Solution: Greedy
        Time Complexity: O(n)
        Space Complexity: O(1)
        TP:
        - Using greedy to update farthest point we can reach at each jump
        :type nums: List[int]
        :rtype: int
        """
        if not nums or len(nums)==1:
            return 0
        jump=nextfar=curfar=0
        m=len(nums)
        for i in range(m):
            nextfar=max(i+nums[i],nextfar)
            if nextfar >= m-1:
                return jump+1
            if i == curfar:
                jump+=1
                curfar=nextfar

# -*- coding: utf-8 -*-
class Solution(object):
    def maxChunksToSorted(self, arr):
        """
        :type arr: List[int]
        :rtype: int
        """
        curr_max = -float('inf')
        k = 0
        for idx, num in enumerate(arr):
            curr_max = max(curr_max, num)
            if idx == curr_max:
                k += 1
        return k


assert Solution().maxChunksToSorted([1,0,2,3,4]) == 1
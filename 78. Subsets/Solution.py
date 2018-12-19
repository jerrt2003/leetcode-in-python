# -*- coding: utf-8 -*-
class Solution(object):
    def subsets(self, nums):
        """
        Solution: Backtracking
        Time Complexity:
        Space Complexity:
        Inspired By: MySELF!! (32ms, beat 41.83%)
        TP:
        - using SET to speed up the process
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        visited = set([])
        def findSub(curr_comb, remain_num):
            if tuple(curr_comb) not in visited:
                visited.add(tuple(curr_comb))
                for i in remain_num:
                    next_comb = curr_comb[:]
                    next_comb.append(i)
                    next_comb.sort()
                    next_remain_num = remain_num[:]
                    next_remain_num.remove(i)
                    findSub(next_comb,next_remain_num)
            else:
                return
        findSub([],nums)
        res = []
        for _res in visited:
            res.append(list(_res))
        return res

nums = [1,2,3]
print Solution().subsets(nums)

# -*- coding: utf-8 -*-
class Solution(object):
    def permute(self, nums):
        """
        Solution: Backtracking
        Time Complexity:
        Space Complexity:
        Inspired By: MySELF!! (36ms, 99.68%)
        TP:
        - Kind like brutal force
        - Good reading: https://leetcode.com/problems/permutations/discuss/18239/A-general-approach-to-backtracking-questions-in-Java-(Subsets-Permutations-Combination-Sum-Palindrome-Partioning)
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = []
        def doPermute(path, lst):
            if len(lst) == 1:
                path.append(lst.pop())
                res.append(path)
            else:
                for i in lst:
                    next_lst = lst[:]
                    next_lst.remove(i)
                    next_path = path[:]
                    next_path.append(i)
                    doPermute(next_path, next_lst)
        doPermute([], nums)
        return res


n = [1,2,3,4,5,6,7,8,9,10,11]
print Solution().permute(n)
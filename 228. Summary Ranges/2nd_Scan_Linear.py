# -*- coding: utf-8 -*-
class Solution(object):
    def summaryRanges(self, nums):
        """
        Solution: Linear O(n)
        Time Complexity: O(n)
        Space Complexity: O(n)
        Inspired By: MySELF!! (28ms, beat 100%)
        :type nums: List[int]
        :rtype: List[str]
        """
        sections = []
        curr_range = []
        for num in nums:
            if not curr_range:
                curr_range.append(num)
            else:
                if num - curr_range[-1] > 1:
                    sections.append(curr_range)
                    curr_range = [num]
                else:
                    if len(curr_range) == 1:
                        curr_range.append(num)
                    else:
                        curr_range[-1] = num
        sections.append(curr_range)
        res = []
        for section in sections:
            if len(section) == 1:
                res.append(str(section[0]))
            else:
                res.append(str(section[0]) + '->' + str(section[1]))
        return res

nums = [0,1,2,4,5,7]
print Solution().summaryRanges(nums)
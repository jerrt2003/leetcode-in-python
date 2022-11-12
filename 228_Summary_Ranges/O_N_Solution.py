# -*- coding: utf-8 -*-
class Solution(object):
    def summaryRanges(self, nums):
        """
        Solution: O(n)
        Time Complexity: O(n)
        Space Complexity: O(n)
        Inspired By: MYSELF!!
        :type nums: List[int]
        :rtype: List[str]
        """
        if nums is None or len(nums) == 0: return []
        res = [str(nums[0])]
        for i in range(1, len(nums)):
            pair = res[-1].split('->')
            if len(pair) > 1:
                isPair = True
            else:
                isPair = False
            if not isPair and int(res[-1])+1 == nums[i]:
                res[-1] = res[-1] + '->' + str(nums[i])
            elif isPair:
                if int(pair[1]) + 1 == nums[i]:
                    res[-1] = pair[0] + '->' + str(nums[i])
                else:
                    res.append(str(nums[i]))
            else:
                res.append(str(nums[i]))
        return res

#nums = [0,1,2,4,5,7]
nums = [-2147483648,-2147483647,2147483647]
sol = Solution()
print sol.summaryRanges(nums)
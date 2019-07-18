# -*- coding: utf-8 -*-
class Solution(object):
    def findAllCombo(self, nums):
        res = []
        nums.sort()
        for i in range(len(nums)-2):
            if i == 0 or nums[i-1] != nums[i]:
                l = i+1
                r = len(nums)-1
                while l < r:
                    sum = nums[i]**2 + nums[l]**2
                    if sum == nums[r]**2:
                        res.append((nums[i],nums[l],nums[r]))
                        break
                    elif sum < nums[r]**2:
                        l += 1
                    else:
                        r -= 1
        return res

assert Solution().findAllCombo([6,7,8,10]) == [(6,8,10)]
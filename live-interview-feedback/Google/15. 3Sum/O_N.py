# -*- coding: utf-8 -*-
class Solution(object):
    def threeSum(self, nums):
        """
        Solution: 2-sum extension
        Time Complexity: O(n^2)
        Space Complexity: O(n)
        Inspired By: MySELF!! (1220ms, beat 18.44%)
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        res = set()
        visited = set()
        nums.sort()
        for i in range(len(nums)):
            target = 0 - nums[i]
            if target not in visited:
                visited.add(target)
                lst = nums[:i] + nums[i+1:]
                p1 = 0
                p2 = len(lst)-1
                while p1 < p2:
                    total = lst[p1] + lst[p2]
                    if total == target:
                        _ans = [nums[i],lst[p1],lst[p2]]
                        _ans.sort()
                        res.add(tuple(_ans))
                        p1 += 1
                        p2 -= 1
                    elif total < target:
                        p1 += 1
                    else:
                        p2 -= 1
        return [list(ans) for ans in res]

#nums = [-1, 0, 1, 2, -1, -4, -2]
#nums = [0,0,1]
nums = [-4,-2,-2,-2,0,1,2,2,2,3,3,4,4,6,6]
print Solution().threeSum(nums)
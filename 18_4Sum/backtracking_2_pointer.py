# -*- coding: utf-8 -*-
class Solution(object):
    def fourSum(self, nums, target):
        """
        Solution: Recursive + Backtracking + 2_pointer
        Time Complexity: O(n*3)
        Space Complexity: O(1)
        Inspired By: https://leetcode.com/problems/4sum/discuss/8545/Python-140ms-beats-100-and-works-for-N-sum-(Ngreater2)
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """
        res = []
        nums.sort()

        def helper(nums, N, target, path, res):
            """
            A helper function which will slice nums if N > 2 or execute 2-pointer algorithm if N == 2
            :param nums:
            :param N:
            :param target:
            :param path:
            :param res:
            :return:
            """
            if N == 2:
                i = 0
                j = len(nums)-1
                while i < j:
                    sum = nums[i] + nums[j]
                    if sum == target:
                        res.append(path[:] + [nums[i], nums[j]])
                        i += 1
                        j -= 1
                        while nums[i-1] == nums[i] and i < j:
                            i += 1
                        while nums[j+1] == nums[j] and i < j:
                            j -= 1
                    elif sum < target:
                            i += 1
                    else:
                            j -= 1
            else:
                for i in range(len(nums) - N + 1):
                    if nums[-1] * N < target or nums[0] * N > target:
                        break
                    elif i == 0 or i > 0 and nums[i - 1] != nums[i]:
                        helper(nums[i+1:], N-1, target-nums[i], path+[nums[i]], res)

        helper(nums, 4, target, [], res)
        return res

nums = [-1,0,-5,-2,-2,-4,0,1,-2]
target = -9
print Solution().fourSum(nums, target)
# -*- coding: utf-8 -*-
class Solution(object):
    def longestConsecutive(self, nums):
        """
        Solution: Set + Array
        Time Complexity: O(n)
        Space Complexity: O(1)
        Inspired By: https://leetcode.com/problems/longest-consecutive-sequence/solution/
        TP:
        - First we need to filter out 'duplicate' numbers since it only count as 1
        - Then we start go through the 'filtered' list and apply following logic:
            - if nums - 1 not in the list, which means it must be the starting number of a new consecutive numbers
            - based on previous observation, we can:
                - create a tmp_res to stored "THIS" consecutive numbers length
                - check if current_num + 1 is in the list or not:
                    - if yes, we add 1 to the tmp_res and move current_num by 1 (current_num += 1)
                    - also for each iteration we'll compare current length to the global length in order to record longest length
        :type nums: List[int]
        :rtype: int
        """
        nums = set(nums)
        res = 1 if len(nums) > 0 else 0 # take care of the boundary condition
        for num in nums:
            if num - 1 not in nums: # if num-1 in nums which means it will be taken care of by other iteration already
                '''
                原來我還想要說可以用類似DP的方式去加速(避免重複的算), 但是有了if nums-1 not in nums的條件實際上我們不會碰到重複的狀況
                '''
                tmp_res = 1
                current_num = num
                while current_num+1 in nums:
                    tmp_res += 1
                    res = max(res, tmp_res)
                    current_num += 1
        return res

nums = [-6,-1,-1,9,-8,-6,-6,4,4,-3,-8,-1]
#nums = [0]
sol = Solution()
print sol.longestConsecutive(nums)
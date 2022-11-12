# -*- coding: utf-8 -*-
class Solution(object):
    def majorityElement(self, nums):
        """
        Solution: Boyer-Moore Linear
        Time Complexity: O(n)
        Space Complexity: O(1)
        Inspired By: https://leetcode.com/problems/majority-element-ii/discuss/63520/Boyer-Moore-Majority-Vote-algorithm-and-my-elaboration
        TP:
        - Follow up reading; https://gregable.com/2013/10/majority-vote-algorithm-find-majority.html
        :type nums: List[int]
        :rtype: List[int]
        """
        if not nums:
            return
        count1, count2, candidate1, candidate2 = 0, 0, 0, 1
        for num in nums:
            if num == candidate1:
                count1 += 1
            elif num == candidate2:
                count2 += 1
            elif count1 == 0:
                candidate1, count1 = num, 1
            elif count2 == 0:
                candidate2, count2 = num, 1
            else:
                count1 -= 1
                count2 -= 1

        return [res for res in (candidate1, candidate2) if nums.count(res) > len(nums)/3]

nums = [1,1,1,3,3,2,2,2]
print Solution().majorityElement(nums)
# -*- coding: utf-8 -*-
class Solution(object):
    def majorityElement(self, nums):
        """
        Solution: Boyer-Moore 2nd pass to confirm the majority
        Time Complexity: O(n)
        Space Complexity: O(1)
        TP:
        - Follow up reading: https://stackoverflow.com/questions/46615387/requirement-of-second-pass-for-the-boyer-moore-majority-vote-algorithm
        :type nums: List[int]
        :rtype: List[int]
        """
        cand, count = 0, 0
        for num in nums:
            if num == cand:
                count +=1
            elif count == 0:
                cand, count = num, 1
            else:
                count -= 1
        # 2nd pass to confirm there is true majority elements
        for num in nums:
            if num != cand:
                count -= 1
        if count < 0:
            return "No majority elements present"
        else:
            return cand

nums = [1, 2, 2, 3, 3, 4, 4, 5, 5, 5, 5, 5, 5, 5, 5, 5]
print Solution().majorityElement(nums)

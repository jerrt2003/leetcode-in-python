# -*- coding: utf-8 -*-
class Solution(object):
    def twoSum(self, numbers, target):
        """
        Solution: Use 2-pointer
        Time Complexity: O(n)
        Space Complexity: O(1)
        Inspired By: MYSELF!!
        :type numbers: List[int]
        :type target: int
        :rtype: List[int]
        """
        i, j = 1, len(numbers)
        while i < j:
            if numbers[i-1] + numbers[j-1] == target:
                return [i, j]
            elif numbers[i-1] + numbers[j-1] > target:
                j -= 1
            else:
                i += 1
        return []

numbers = [2,7,11,15]
target = 9

sol = Solution()
print sol.twoSum(numbers, target)
# -*- coding: utf-8 -*-
class Solution(object):
    def firstMissingPositive(self, nums):
        """
        Solution: O(n)
        Time Complexity: O(n)
        Space Complexity: O(1)
        Inspired By:
        - https://leetcode.com/problems/first-missing-positive/discuss/17071/My-short-c++-solution-O(1)-space-and-O(n)-time
        - https://leetcode.com/problems/first-missing-positive/discuss/17071/My-short-c++-solution-O(1)-space-and-O(n)-time/181115
        TP:
        - The main idea is to try to put as many number at its right position as possible, the the first number which is not at its (right position+1) is the min missing number
        - ex. [3,1,5,7] --> [5,1,3,7] --> [1,5,3,7]
        - since 5 is the first number not at its right position (and its idx is 1) thus we know 2 (1+1) is the first missing number
        :type nums: List[int]
        :rtype: int
        """
        i = 1
        while i <= len(nums):
            '''
            為什麼使用While而不是For loop?
            因為while loop才能保證對的數安插到對的位置
            ex.[3,4,-1,1]
            loop 1: [-1,4,3,1]
            loop 2: [-1,1,3,4] -> [1,-1,3,4] <== 若是用for loop我們會沒有辦法把1給安插到對的位置 (e.g. stop @ [-1,1,3,4]
            '''
            x = nums[i - 1]
            if x != i and 1 <= x <= len(nums) and nums[x - 1] != x:
                nums[i - 1], nums[x - 1] = nums[x - 1], x
            else:
                i += 1
        for i, x in enumerate(nums, 1):
            if i != x:
                return i
        return len(nums) + 1

nums = [3,4,-1,1]
#nums = [3,1,5,7]
sol = Solution()
print sol.firstMissingPositive(nums)
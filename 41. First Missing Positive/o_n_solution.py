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
        - The main idea is to try to put as many number at its right position as possible, then the first number which is not at its (right position+1) is the min missing number
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
                '''
                condition 解釋:
                1) x != i: 若位置i的數字不是i (ex. nums[1] != 1)
                2) 1 <= x <= len(nums): 若位置i的數字在nums的範圍之中
                   ex. 有可能我們會有不在範圍中的數字: [3,4,-1,1] --> -1 不在 1 ~ 4之間, 所以沒有辦法找到-1應該安插的位置
                3) nums[x-1] != x: 在位置x的數字並不是x
                   ex. 若是nums[5] = 5 --> 我們就不必要更換他了,因為nums[5]已經有對的數字了
                '''
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
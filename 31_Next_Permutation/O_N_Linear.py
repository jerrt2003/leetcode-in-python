class Solution(object):
    def nextPermutation(self, nums):
        """
        Facebook
        Runtime: 32 ms, faster than 62.32% of Python online submissions for Next Permutation.
        Memory Usage: 12.9 MB, less than 11.29% of Python online submissions for Next Permutation.
        Solution: O(n) Linear Solution
        Time Complexity: O(n)
        Space Complexity: O(1)
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        i = len(nums) - 1
        while i > 0: #!!!!!
            if nums[i - 1] < nums[i]:
                break
            else:
                i -= 1
        if i == 0: # already largest array, just swap
            l = 0
            r = len(nums)-1
        else:
            j = len(nums) - 1
            while j >= i:
                if nums[j] > nums[i - 1]:
                    break
                else:
                    j -= 1
            nums[i - 1], nums[j] = nums[j], nums[i - 1]
            l = i
            r = len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

Solution().nextPermutation([3,2,1])

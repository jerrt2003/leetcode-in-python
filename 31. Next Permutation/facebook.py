class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: None Do not return anything, modify nums in-place instead.
        """

        # finding inversion point swapping and then appending in reverse trick
        # the initial inversion point
        inversion_point = len(nums) - 2

        # to find the first decreasing element from the end
        while inversion_point >= 0 and nums[inversion_point] >= nums[inversion_point + 1]:
            inversion_point -= 1

        # if reached the left most end then it means that the current configuration is the next perm
        if inversion_point == -1: nums.sort(); return

        # swap the element after the inversion point that is greater than the inversion point and then append the frist half to the second one reversed

        for i in reversed(range(inversion_point + 1, len(nums))):
            if nums[i] > nums[inversion_point]:
                nums[inversion_point], nums[i] = nums[i], nums[inversion_point]; break

        nums[inversion_point + 1:] = reversed(nums[inversion_point + 1:])

print Solution().nextPermutation([1,2,7,4,3,1])
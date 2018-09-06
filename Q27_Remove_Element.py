class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """
        if nums is None or len(nums) == 0:
            return 0
        res = 0
        for i in range(0, len(nums)):
            if nums[i] != val:
                nums[res] = nums[i]
                res += 1
        return res
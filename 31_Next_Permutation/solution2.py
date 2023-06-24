from typing import List


class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i, j, k = len(nums) - 2, len(nums) - 1, len(nums) - 1
        while i >= 0 and nums[i] >= nums[j]:
            i -= 1
            j -= 1
        # 檢查數列是否已經是最大的排列(e.g. 6,5,4,3,2,1)
        if i >= 0:
            while nums[i] >= nums[k]:
                k -= 1
            nums[i], nums[k] = nums[k], nums[i]
        l, r = j, len(nums) - 1
        while l < r:
            nums[l], nums[r] = nums[r], nums[l]
            l += 1
            r -= 1

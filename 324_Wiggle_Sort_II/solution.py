from typing import List


class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums.sort()
        m = len(nums) // 2
        a = nums[: m + 1][::-1]
        b = nums[m + 1 :][::-1]

        i = 0
        while (a or b) and i < len(nums):
            if a:
                nums[i] = a.pop(0)
                i += 1
            if b:
                nums[i] = b.pop(0)
                i += 1

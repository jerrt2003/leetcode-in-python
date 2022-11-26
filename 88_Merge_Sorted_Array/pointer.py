from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        j = 0 # the idx for first 0
        for i, num in enumerate(nums):
            if num != 0:
                nums[i], nums[j] = nums[j], nums[i]
                j += 1
        print(nums)                

if __name__ == "__main__":
    s = Solution()
    s.moveZeroes([0,1,0,3,12])
    s.moveZeroes([0])
    s.moveZeroes([1,3,12,0,0])
    s.moveZeroes([4,0,1,9,2,0])
from typing import List

class NumArray:

    def __init__(self, nums: List[int]):
        self.nums = nums
        self.prefix_sum: List[int] = []
        for num in self.nums:
            if len(self.prefix_sum) == 0:
                self.prefix_sum.append(num)
            else:
                self.prefix_sum.append(self.prefix_sum[-1] + num)

    def sumRange(self, left: int, right: int) -> int:
        left_sum = self.prefix_sum[left]
        right_sum = self.prefix_sum[right]
        return right_sum - left_sum + self.nums[left]
        


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# param_1 = obj.sumRange(left,right)
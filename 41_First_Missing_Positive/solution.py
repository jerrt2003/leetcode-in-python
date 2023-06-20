from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        size = len(nums)
        for i in range(len(nums)):
            # 先判断这个数字是不是索引，然后判断这个数字是不是放在了正确的地方
            # 
            # PS1. 为什么使用 while ？ 因为交换后，原本 i 位置的 nums[i] 已经交换到了别的地方，
            # 交换后到这里的新值不一定是适合这个位置的，因此需要重新进行判断交换
            # 如果使用 if，那么进行一次交换后，i 就会 +1 进入下一个循环，那么交换过来的新值就没有去找到它该有的位置
            # 比如 nums = [3, 4, -1, 1] 当 3 进行交换后， nums 变成 [-1，4，3，1]，
            # 此时 i == 0，如果使用 if ，那么会进入下一个循环， 这个 -1 就没有进行处理
            while 1 <= nums[i] and nums[i] <= size and nums[i] != nums[nums[i]-1]:
                # Python 里可以这样写 nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1] ，
                # 但是这里赋值有先后顺序，写成 nums[i], nums[nums[i] - 1] = nums[nums[i] - 1], nums[i], 就会出错。建议封装成单独的函数，避免出错。
                self._swap(nums, i, nums[i]-1)

        for i in range(len(nums)):
            if nums[i] != i+1:
                return i+1
            
        return size+1

    def _swap(self, nums: List[int], a: int, b: int):
        # 以下swap的邏輯同等於:
        # temp = nums[a]
        # nums[a] = nums[b]
        # nums[b] = temp
        nums[a], nums[b] = nums[b], nums[a]
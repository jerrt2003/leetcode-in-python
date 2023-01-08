from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        # 恢復數列的二段性
        # [4,5,6,7,1,2,3,4,4] -> 無法判斷哪邊為旋轉點 
        # -> [4,5,6,7,1,2,3] 恢復二分性 -> 可以判斷且不影響結果
        l, r = 0, len(nums)-1
        while l < r and nums[l] == nums[r]:
            r -= 1
        lb, rb = l, r+1
        while lb < rb:
            m = (lb+rb-1)//2
            if nums[m] < nums[l]:
                rb = m
            else:
                lb = m+1
        return nums[l] if lb == r+1 else nums[lb]
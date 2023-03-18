from typing import List

class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        ans = 1
        count = 1
        for i in range(0, len(nums)-1):
            if nums[i] <= nums[i+1]:
                count += 1
                continue
            else:
                ans = max(ans, count)
                count = 1
        # 在最後一個數字的時候，要再做一次比較，因為最後一個數字不會進入到上面的迴圈
        return max(ans, count)
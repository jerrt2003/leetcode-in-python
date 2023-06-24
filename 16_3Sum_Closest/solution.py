from typing import List

class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        # sort nums
        nums.sort()
        # go through idx
        ans = float('inf')
        for i in range(0, len(nums)-2):
            j, k = i+1, len(nums)-1
            tmp_sum = 0
            while j < k:
                tmp_sum = nums[i] + nums[j] + nums[k]
                if tmp_sum == target:
                    return tmp_sum
                if abs(ans-target) > abs(tmp_sum-target):
                    ans = tmp_sum
                if tmp_sum > target:
                    k -= 1
                else:
                    j += 1
        return ans
class Solution:
    def findLengthOfLCIS(self, nums: List[int]) -> int:
        ans = 0
        count = 1
        for i in range(1, len(nums)):
            if nums[i] > nums[i - 1]:
                count += 1
            else:
                ans = max(ans, count)
                count = 1
        return max(ans, count)

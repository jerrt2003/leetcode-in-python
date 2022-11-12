class Solution(object):
    def findArray(self, nums, target):
        total = 0
        j = 0
        ans = []
        for i, v in enumerate(nums):
            total += v
            while total >= target:
                if total == target:
                    ans.append(nums[j:i+1])
                total -= nums[j]
                j += 1
        return ans


print Solution().findArray([1,2,1], 3)
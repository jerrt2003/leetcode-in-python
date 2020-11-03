class Solution(object):
    def minSubArrayLen(self, s, nums):
        """
        T:O(n) S:O(1)
        Runtime: 64 ms, faster than 43.41% of Python online submissions for Minimum Size Subarray Sum.
        Memory Usage: 14.8 MB, less than 5.26% of Python online submissions for Minimum Size Subarray Sum.
        :type s: int
        :type nums: List[int]
        :rtype: int
        """
        l, j, ans = len(nums), 0, float('inf')
        for i in range(l):
            s -= nums[i]
            while j <= i and s <= 0:
                ans = min(ans, i-j+1)
                s += nums[j]
                j += 1
        return ans if ans != float('inf') else 0

# print Solution().minSubArrayLen(7, [2,3,1,2,4,3])
# print Solution().minSubArrayLen(4, [1,4,4])
# print Solution().minSubArrayLen(3, [2,-1,2])
print Solution().minSubArrayLen(167, [84,-37,32,40,95])
class Solution(object):
    def movesToMakeZigzag(self, nums):
        """
        T:O(n) S:O(2)
        Runtime: 16 ms, faster than 90.00% of Python online submissions for Decrease Elements To Make Array Zigzag.
        Memory Usage: 12.9 MB, less than 100.00% of Python online submissions for Decrease Elements To Make Array Zigzag.
        :type nums: List[int]
        :rtype: int
        """
        res = [0, 0]
        nums = [float('inf')] + nums + [float('inf')]
        for i in range(1, len(nums)-1):
            res[i%2] += max(0, nums[i]-min(nums[i-1], nums[i+1])+1)
        return min(res)
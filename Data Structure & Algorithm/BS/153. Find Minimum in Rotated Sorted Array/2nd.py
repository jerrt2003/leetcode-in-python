class Solution(object):
    def findMin(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        l, r = 0, len(nums)
        while l < r:
            m = (l+r-1)/2
            if nums[m] < nums[r-1]:
                r = m
            else:
                l = m+1
        return nums[-1] if l == len(nums) else nums[l]

#assert Solution().findMin([2,3,1]) == 1
assert Solution().findMin([3,4,5,1,2]) == 1
#assert Solution().findMin([3,1,2]) == 1
#assert Solution().findMin([4,5,6,7,0,1,2]) == 0
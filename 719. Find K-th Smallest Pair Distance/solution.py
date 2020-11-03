class Solution(object):
    def smallestDistancePair(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        nums.sort()
        l, r = 0, (nums[-1]-nums[0])+1

        def isValid(mid):
            pair, start = 0, 0
            for i in range(len(nums)):
                while nums[i] - nums[start] > mid:
                    start += 1
                pair += (i-start)
            return pair >= k

        while l < r:
            mid = (l+r-1)/2
            if isValid(mid):
                r = mid
            else:
                l = mid+1
        return l

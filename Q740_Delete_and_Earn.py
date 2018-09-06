class Solution(object):
    def deleteAndEarn(self, nums):
        """
        An transform from 198 House Ron Problem
        :type nums: List[int]
        :rtype: int
        """
        points = [0]*(10000+1) # list idx will start with 0 thus need to use 10000+1
        for num in nums:
            points[num] += num
        return self._deleteAndEarn(points)

    def _deleteAndEarn(self, points):
        add = 0
        not_add = 0
        for point in points:
            tmp = add
            add = not_add + point
            not_add = max(tmp, not_add)
        return max(add, not_add)


nums = [2, 2, 3, 3, 3, 4]
sol = Solution()
print sol.deleteAndEarn(nums)
class Solution(object):
    def rob(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        rob = 0
        not_rob = 0
        for money in nums:
            tmp = rob
            rob = not_rob + money
            not_rob = max(tmp, not_rob)
        return max(rob, not_rob)


a = [2,7,9,3,1]
sol = Solution()
print sol.rob(a)

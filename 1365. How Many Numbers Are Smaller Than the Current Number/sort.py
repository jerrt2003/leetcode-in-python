class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        T:O(nlog(n)) S:O(n)
        Runtime: 44 ms, faster than 78.90% of Python online submissions for How Many Numbers Are Smaller Than the Current Number.
        Memory Usage: 12.7 MB, less than 100.00% of Python online submissions for How Many Numbers Are Smaller Than the Current Number.
        :type nums: List[int]
        :rtype: List[int]
        """
        ans_map = dict()
        sort_nums = nums[:]
        sort_nums.sort()
        ans_map[sort_nums[0]] = 0
        for i in range(1, len(sort_nums)):
            if sort_nums[i] == sort_nums[i-1]:
                continue
            else:
                ans_map[sort_nums[i]] = i
        res = []
        for num in nums:
            res.append(ans_map[num])
        return res


print Solution().smallerNumbersThanCurrent([8,1,2,2,3])
print Solution().smallerNumbersThanCurrent([6,5,4,8])
print Solution().smallerNumbersThanCurrent([7,7,7,7])
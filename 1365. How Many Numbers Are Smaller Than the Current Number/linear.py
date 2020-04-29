class Solution(object):
    def smallerNumbersThanCurrent(self, nums):
        """
        T:O(n) S:O(n)
        Runtime: 32 ms, faster than 99.24% of Python online submissions for How Many Numbers Are Smaller Than the Current Number.
        Memory Usage: 12.7 MB, less than 100.00% of Python online submissions for How Many Numbers Are Smaller Than the Current Number.
        :type nums: List[int]
        :rtype: List[int]
        """
        counter = [0]*101
        for num in nums:
            counter[num] += 1
        total = 0
        maps = [0]*101
        for i, v in enumerate(counter):
            maps[i] = total
            total += v
        res = [0]*len(nums)
        for i, v in enumerate(nums):
            res[i] = maps[v]
        return res


print Solution().smallerNumbersThanCurrent([8,1,2,2,3])
print Solution().smallerNumbersThanCurrent([6,5,4,8])
print Solution().smallerNumbersThanCurrent([7,7,7,7])
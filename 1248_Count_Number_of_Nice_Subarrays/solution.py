class Solution(object):
    def numberOfSubarrays(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        return self.atMostK(nums, k) - self.atMostK(nums, k-1)


    def atMostK(self, nums, k):
        l = len(nums)
        j = 0
        res = 0
        for i in range(l):
            if nums[i] % 2 == 1:
                k -= 1
            while k < 0:
                if nums[j] % 2 == 1:
                    k += 1
                j += 1
            res += i - j + 1
        return res

print Solution().numberOfSubarrays([2,2,2,1,2,2,1,2,2,2],2)
# print Solution().numberOfSubarrays([1,1,2,1,1], 3)
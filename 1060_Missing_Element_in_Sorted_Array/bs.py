class Solution(object):
    def missingElement(self, nums, k):
        """
        Facebook
        BS
        T:O(n+nlog(n)) S:O(n)
        Runtime: 324 ms, faster than 19.20% of Python online submissions for Missing Element in Sorted Array.
        Memory Usage: 18.7 MB, less than 100.00% of Python online submissions for Missing Element in Sorted Array.
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        miss_arr = [0]
        miss_count = 0
        for i in range(len(nums)-1):
            if nums[i+1] - nums[i] > 1:
                miss_count += nums[i+1]-nums[i]-1
            miss_arr.append(miss_count)
        l, r = 0, len(miss_arr)
        while l < r:
            m = (l+r-1)//2
            if miss_arr[m] >= k:
                r = m
            else:
                l = m+1
        if l == len(miss_arr) or miss_arr[l] != k:
            return nums[l-1]+(k-miss_arr[l-1])
        else:
            return nums[l]-1

print(Solution().missingElement([4,7,9,10],1))
print(Solution().missingElement([4,7,9,10],3))
print(Solution().missingElement([1,2,4],3))
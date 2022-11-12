class Solution(object):
    def findClosestElements(self, arr, k, x):
        """
        Facebook
        BS
        T:O(log(n)+K) S:O(1)
        Runtime: 400 ms, faster than 30.48% of Python online submissions for Find K Closest Elements.
        Memory Usage: 14.2 MB, less than 37.76% of Python online submissions for Find K Closest Elements.
        :type arr: List[int]
        :type k: int
        :type x: int
        :rtype: List[int]
        """
        l, r = 0, len(arr)
        while l < r:
            m = (l + r - 1) / 2
            if arr[m] >= x:
                r = m
            else:
                l = m + 1
        left, right = max(0, l-k), min(len(arr)-1, l+k)
        while right - left + 1 > k:
            if x - arr[left] > arr[right] - x:
                left += 1
            else:
                right -= 1
        return arr[left:right+1]
        # while l < r:
        #     m = (l+r-1)/2
        #     if arr[m+k] - x >= x - arr[m]:
        #         r = m
        #     else:
        #         l = m+1
        # return arr[m:m+k]



print Solution().findClosestElements([1,2,3,4,5,6,7,8,9],5,4)
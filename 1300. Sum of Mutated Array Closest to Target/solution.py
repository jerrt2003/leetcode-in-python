class Solution(object):
    def findBestValue(self, arr, target):
        """
        BS
        T:O(log(n)*log(n)), S:O(1)
        Runtime: 80 ms, faster than 96.15% of Python online submissions for Sum of Mutated Array Closest to Target.
        Memory Usage: 13.5 MB, less than 100.00% of Python online submissions for Sum of Mutated Array Closest to Target.
        :type arr: List[int]
        :type target: int
        :rtype: int
        """
        arr.sort()
        def sumArray(arr, i):
            # return sum(min(x, i) for x in arr) <- take linear time
            l, r = 0, len(arr)
            while l < r:
                m = (l+r-1)/2
                if arr[m] >= i:
                    r = m
                else:
                    l = m+1
            return sum(arr[:l])+i*(len(arr)-l)
        l, r = 0, max(arr)+1
        while l < r:
            m = (l+r-1)/2
            if sumArray(arr, m) > target:
                r = m
            else:
                l = m+1
        return min(l-1, l, l+1, key=lambda x: abs(target-sumArray(arr, x)))

print Solution().findBestValue([4,9,3], 10)
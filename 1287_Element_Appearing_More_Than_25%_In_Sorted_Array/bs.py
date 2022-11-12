class Solution(object):
    def findSpecialInteger(self, arr):
        """
        T:O(nlogn) S:O(1)
        Runtime: 84 ms, faster than 46.00% of Python online submissions for Element Appearing More Than 25% In Sorted Array.
        Memory Usage: 13.7 MB, less than 100.00% of Python online submissions for Element Appearing More Than 25% In Sorted Array.
        :type arr: List[int]
        :rtype: int
        """

        def bs(i):
            l, r = 0, len(arr)
            while l < r:
                m = (l+r-1)//2
                if arr[m] > i:
                    r = m
                else:
                    l = m+1
            return l-1

        i = 0
        while i < len(arr):
            num = arr[i]
            lastIdx = bs(num)
            if lastIdx - i+1 > len(arr)//4:
                return num
            else:
                i = lastIdx+1
        return -1


print(Solution().findSpecialInteger([1,2,2,6,6,6,6,7,10]))
print(Solution().findSpecialInteger([1]))
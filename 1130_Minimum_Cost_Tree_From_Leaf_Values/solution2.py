class Solution(object):
    def mctFromLeafValues(self, arr):
        """
        T:O(n^2) S:O(n)
        Runtime: 20 ms, faster than 81.80% of Python online submissions for Minimum Cost Tree From Leaf Values.
        Memory Usage: 12.8 MB, less than 41.34% of Python online submissions for Minimum Cost Tree From Leaf Values.
        :type arr: List[int]
        :rtype: int
        """
        res = 0
        while len(arr) > 1:
            i = arr.index(min(arr))
            res += min(arr[i-1:i]+arr[i+1:i+2])*arr.pop(i)
        return res

print Solution().mctFromLeafValues([6,2,4])
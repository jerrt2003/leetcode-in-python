class Solution(object):
    def getStrongest(self, arr, k):
        """
        O(nlogn) S:O(1)
        Runtime: 1004 ms, faster than 91.31% of Python online submissions for The k Strongest Values in an Array.
        Memory Usage: 25.5 MB, less than 100.00% of Python online submissions for The k Strongest Values in an Array.
        :type arr: List[int]
        :type k: int
        :rtype: List[int]
        """
        arr.sort()
        n = len(arr)
        mid = arr[(n-1)/2]
        ans = []
        l, r = 0, len(arr)-1
        while l <= r:
            if abs(arr[l]-mid) > abs(arr[r]-mid):
                ans.append(arr[l])
                l += 1
            else:
                ans.append(arr[r])
                r -= 1
            k -= 1
            if k == 0:
                break
        return ans
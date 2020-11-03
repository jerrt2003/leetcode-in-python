class Solution(object):
    def decompressRLElist(self, nums):
        """
        T:O(n) S:O(n)
        Runtime: 52 ms, faster than 88.91% of Python online submissions for Decompress Run-Length Encoded List.
        Memory Usage: 13 MB, less than 100.00% of Python online submissions for Decompress Run-Length Encoded List.
        :type nums: List[int]
        :rtype: List[int]
        """
        ans = []
        for i in range(0, len(nums)-1, 2):
            ans.extend([nums[i+1]]*nums[i])
        return ans

print Solution().decompressRLElist([1,2,3,4])
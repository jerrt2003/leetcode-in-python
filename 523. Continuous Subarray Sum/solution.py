# class Solution(object):
#     def checkSubarraySum(self, nums, k):
#         """
#         :type nums: List[int]
#         :type k: int
#         :rtype: bool
#         """
#         seen = {0: -1}
#         subarray_sum = 0
#         for i, v in enumerate(nums):
#             subarray_sum += v
#             if k != 0:
#                 subarray_sum %= k
#             if subarray_sum in seen and i - seen[subarray_sum] > 1:
#                 return True
#             else:
#                 seen[subarray_sum] = i
#         return False

class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        Facebook
        Array
        T:O(n) S:O(n)
        Runtime: 196 ms, faster than 79.12% of Python online submissions for Continuous Subarray Sum.
        Memory Usage: 12.9 MB, less than 74.59% of Python online submissions for Continuous Subarray Sum.
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        seen = {0: -1}
        rem = 0
        for i, num in enumerate(nums):
            rem += num
            if k != 0:
                rem %= k
            if rem not in seen:
                seen[rem] = i
            if i - seen[rem] > 1:
                return True
        return False

# print Solution().checkSubarraySum([23,2,6,4,7], 0)
print Solution().checkSubarraySum([0,0], 0)
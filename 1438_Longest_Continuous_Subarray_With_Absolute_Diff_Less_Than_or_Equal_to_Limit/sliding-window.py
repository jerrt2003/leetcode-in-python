import collections


class Solution(object):
    def longestSubarray(self, nums, limit):
        """
        Sliding Window
        T:O(n) S:O(n)
        Runtime: 808 ms, faster than 17.75% of Python online submissions for Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit.
        Memory Usage: 20.6 MB, less than 100.00% of Python online submissions for Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit.
        :type nums: List[int]
        :type limit: int
        :rtype: int
        """
        pt1 = pt2 = 0
        curr_nums = collections.defaultdict(int)
        max_num = -float('inf')
        min_num = float('inf')
        ret = -float('inf')
        while pt2 < len(nums):
            curr_nums[nums[pt2]] += 1
            if nums[pt2] > max_num:
                max_num = nums[pt2]
            if nums[pt2] < min_num:
                min_num = nums[pt2]
            while pt1 < pt2 and max_num - min_num > limit:
                curr_nums[nums[pt1]] -= 1
                if curr_nums[nums[pt1]] == 0:
                    del curr_nums[nums[pt1]]
                    if nums[pt1] == max_num:
                        max_num = max(curr_nums.keys())
                    if nums[pt1] == min_num:
                        min_num = min(curr_nums.keys())
                pt1 += 1
            if max_num - min_num <= limit:
                ret = max(ret, pt2-pt1+1)
            pt2 += 1

        return 0 if ret == -float('inf') else ret

print Solution().longestSubarray([8,2,4,7], 4)
print Solution().longestSubarray([10,1,2,4,7,2],5)
print Solution().longestSubarray([],1)

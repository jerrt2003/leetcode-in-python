import collections


class Solution(object):
    def longestSubarray(self, nums, limit):
        """
        sliding window + mono q
        T:O(n) S:O(n)
        Runtime: 652 ms, faster than 27.69% of Python online submissions for Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit.
        Memory Usage: 21.2 MB, less than 100.00% of Python online submissions for Longest Continuous Subarray With Absolute Diff Less Than or Equal to Limit.
        :type nums: List[int]
        :type limit: int
        :rtype: int
        """
        l = r = 0
        min_q = collections.deque()
        max_q = collections.deque()
        ret = -float('inf')
        while r < len(nums):
            while min_q and min_q[-1] > nums[r]:
                min_q.pop()
            while max_q and max_q[-1] < nums[r]:
                max_q.pop()
            min_q.append(nums[r])
            max_q.append(nums[r])
            while max_q[0] - min_q[0] > limit:
                if nums[l] == min_q[0]:
                    min_q.popleft()
                if nums[l] == max_q[0]:
                    max_q.popleft()
                l += 1
            ret = max(ret, r - l + 1)
            r += 1
        return ret
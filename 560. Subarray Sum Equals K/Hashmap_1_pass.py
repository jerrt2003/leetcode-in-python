# -*- coding: utf-8 -*-
import collections
class Solution(object):
    def subarraySum(self, nums, k):
        """
        Solution: Hashmap O(n) 1 pass
        Time Complexity: O(n)
        Space Complexity: O(n)
        Inspired By: https://leetcode.com/problems/subarray-sum-equals-k/solution/ (3692ms, beat 18.56%)
        TP:
        - using hashmap to store the sum happened as we move forward in nums
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        sum_occur = collections.defaultdict(int)
        sum_occur[0] = 1
        sum = count = 0
        for num in nums:
            sum += num
            if (sum-k) in sum_occur.keys():
                count += sum_occur[sum-k]
            sum_occur[sum] += 1 # 需要最後加入hashmap不然會重複算
        return count

nums = [3,4,7,2,-3,1,4,2]
k = 7
print Solution().subarraySum(nums, k)
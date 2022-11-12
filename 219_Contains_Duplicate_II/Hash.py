# -*- coding: utf-8 -*-
class Solution(object):
    def containsNearbyDuplicate(self, nums, k):
        """
        Solution: Hash
        Time Complexity:
        Space Complexity:
        Inspired By:MYSELF!!
        TP:
        - go through the nums
        - use num as key to store in the dict
            - if key exist
                - check if current idx - last idx stored in k/v <= k, if true return True
                - if not continue
            - if key doesn't exist
                - create new k/v use nums[idx] as key and [idx] as value
        - !!! this question is not about the maximum of absolute difference between i, j, but instead it is about whether there are two indexes i, j with nums[i] == nums[j] and abs(i - j) <= k. For example, the input is [1, 0, 1, 1], nums[2] = 1, nums[3] = 1, thus i, j = 2, 3 and abs(i- j) <=1. there exist two indexes match the requirements, thus the output is true.
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        group = {}
        for idx in range(len(nums)):
            if group.has_key(nums[idx]):
                if idx - group[nums[idx]][-1] <= k:
                    return True
                else:
                    group[nums[idx]].append(idx)
            else:
                group[nums[idx]] = [idx]
        return False


#input = [1,0,1,1]
#k = 1
input = [1,2,3,1]
k = 3
#input = [1,2,3,1,2,3]
#k = 2
sol = Solution()
print sol.containsNearbyDuplicate(input, k)
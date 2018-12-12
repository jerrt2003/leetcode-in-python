# -*- coding: utf-8 -*-
class Solution(object):
    def containsDuplicate(self, nums):
        """
        Solution: Hashtable
        Time Complexity: O(n)
        Space Complexity: O(n)
        Inspired By: MYSELF!!
        Thinking process:
        - Create a dict
        - Go through the nums and use num as key
        - If key exist in the list, return True
        - Else add key/value into dict
        - return False at the end
        - USE SET !! len(set(nums)) != len(nums) --> has duplicate !!
        :type nums: List[int]
        :rtype: bool
        """
        duplicate = {}
        for num in nums:
            if duplicate.has_key(num): # need to use haskey to utilize O(1) power!!
                return True
            else:
                duplicate[num] = 1
        return False

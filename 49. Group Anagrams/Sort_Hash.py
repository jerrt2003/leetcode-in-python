# -*- coding: utf-8 -*-
class Solution(object):
    def groupAnagrams(self, strs):
        """
        Solution: Hashtable + sorted + tuple
        Time Complexity: O(NKlogK), where NN is the length of strs, and KK is the maximum length of a string in strs. The outer loop has complexity O(N)O(N) as we iterate through each string. Then, we sort each string in O(K \log K)O(KlogK) time.
        Space Complexity: O(NK)
        Inspired By: https://leetcode.com/problems/group-anagrams/solution/
        TP:
        - two words are anagram of each other only when their sorted string are the same
        - thus we can use sorted(str) as key to check if this key exist in the dict or not
            - if yes we append the string to the k/v
            - if ont we create a new k/v use new string
        - return dict.values()
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        res = {}
        for string in strs:
            key = tuple(sorted(string))
            if res.has_key(key):
                res[key].append(string)
            else:
                res[key] = [string]
        return res.values()

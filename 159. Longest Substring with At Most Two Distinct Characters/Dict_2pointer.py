# -*- coding: utf-8 -*-
class Solution(object):
    def lengthOfLongestSubstringTwoDistinct(self, s):
        """
        Solution: Hashtable + String + 2pointer
        Time Complexity: O(n)
        Space Complexity: O(1)
        Inspired By: MySELF!! (88ms, beat 11%)
        TP:
        - Using a 2-pointer to go through the string
        - Using a hash table to track how many distinct chars we encounter so far. The len of distinct char can't be larger than 2
        :type s: str
        :rtype: int
        """
        if len(s) == 0:
            return 0
        count_dict = dict()
        p1 = p2 = max_len = 0
        count_dict[s[p2]] = 1
        while True:
            if len(count_dict) < 3:
                max_len = max(max_len, p2-p1+1)
                p2 += 1
                if p2 >= len(s):
                    break
                if s[p2] in count_dict:
                    count_dict[s[p2]] += 1
                else:
                    count_dict[s[p2]] = 1
            else:
                count_dict[s[p1]] -= 1
                if count_dict[s[p1]] == 0:
                    count_dict.pop(s[p1])
                p1 += 1
        return max_len

s = "ccaabbb"
print Solution().lengthOfLongestSubstringTwoDistinct(s)
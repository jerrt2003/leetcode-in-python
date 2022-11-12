# -*- coding: utf-8 -*-
class Solution(object):
    def firstUniqChar(self, s):
        """
        Solution: O(n)
        Time Complexity:
        Space Complexity:
        Inspired By: MYSELF + https://leetcode.com/problems/first-unique-character-in-a-string/discuss/86351/Python-3-lines-beats-100-(~-60ms)-!
        TP:
        - There are two ways of solving this question:
            - Using dict
            - Using count (TLE)
        :type s: str
        :rtype: int
        """
        '''
        idx_lst = [s.index(char) for char in s if s.count(char) == 1]
        return min(idx_lst) if len(idx_lst) > 0 else -1
        '''
        idx_lst = dict()
        for char in s:
            try:
                idx_lst[char] += 1
            except:
                idx_lst[char] = 1
        key_lst = []
        for k, v in idx_lst.iteritems():
            if v == 1:
                key_lst.append(s.index(k))
        return min(key_lst) if len(key_lst) > 0 else -1

s = 'loveleetcode'
print Solution().firstUniqChar(s)
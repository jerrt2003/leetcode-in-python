# -*- coding: utf-8 -*-
class Solution(object):
    def canConstruct(self, ransomNote, magazine):
        """
        Solution: Using count
        Time Complexity: O(n)
        Space Complexity:
        Inspired By: https://leetcode.com/problems/ransom-note/discuss/85757/pythonset()count()
        TP:
        - (my old solution)
        for char in ransomNote:
            if char in magazine:
                magazine.pop(magazine.index(char))
            else:
                return False
        return True
        ==> This will only work if the input is LIST !!!!! (STRING doesn't have pop() function since its immutable)
        - Using COUNT instead
        :type ransomNote: str
        :type magazine: str
        :rtype: bool
        """
        char_set = set(ransomNote)
        for char in char_set:
            if ransomNote.count(char) > magazine.count(char):
                return False
        return True

rasomNote = 'aa'
magazine = 'ab'
sol = Solution()
print sol.canConstruct(rasomNote, magazine)
# -*- coding: utf-8 -*-
class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        Solution: Using built-in function ord (return unicode) and Set
        :type words: List[str]
        :rtype: int
        """
        morse_code = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        res = set()
        for word in words:
            val = ''
            for char in word:
                val += morse_code[ord(char) - ord('a')]
            res.add(val)
        return len(res)
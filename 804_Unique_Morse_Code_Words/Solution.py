# -*- coding: utf-8 -*-
class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        Solution: using dict
        Time Complexity: O(n)
        Space Complexity: O(n)
        Inspired By: MYSELF!!
        :type words: List[str]
        :rtype: int
        """
        self.letters = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
        self.morseCode = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        res = dict()
        for word in words:
            key = ''
            for char in word:
                key = key + self.morseCode[self.letters.index(char)]
            res[key] = 1
        return len(res.keys())

#words = ["gin", "zen", "gig", "msg"]
words = []
sol = Solution()
print sol.uniqueMorseRepresentations(words)
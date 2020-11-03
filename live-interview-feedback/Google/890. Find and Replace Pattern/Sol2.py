# -*- coding: utf-8 -*-
class Solution(object):
    def findAndReplacePattern(self, words, pattern):
        """
        :type words: List[str]
        :type pattern: str
        :rtype: List[str]
        """

        def match(word):
            m = dict()
            for p, w in zip(pattern, word):
                if m.setdefault(p, w) != w:
                    return False
            return len(set(m.values())) == len(m.values())

        return filter(match, words)
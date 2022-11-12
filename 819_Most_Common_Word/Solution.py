# -*- coding: utf-8 -*-
import re, collections
class Solution(object):
    def mostCommonWord(self, paragraph, banned):
        """
        :type paragraph: str
        :type banned: List[str]
        :rtype: str
        """
        banset = banned
        word_count = collections.Counter(re.split("; |,|\*|\n |\!|\.|\ |\?|\'", paragraph.lower()))
        res, freq = None, -float('inf')
        for k, v in word_count.iteritems():
            if v > freq and k not in banset and k != '':
                res, freq = k, v
        return res


print Solution().mostCommonWord(a, b)
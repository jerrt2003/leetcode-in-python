# -*- coding: utf-8 -*-
class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = []
        cache = ''
        for _s in s:
            if _s == ' ' and len(cache) != 0:
                res.append(cache)
                cache = ''
            elif _s != ' ':
                cache += _s
        if cache:
            res.append(cache)
        return ' '.join(res[::-1])


assert Solution().reverseWords("the sky is blue") == "blue is sky the"
# -*- coding: utf-8 -*-
class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        if len(digits) == 0:
            return []
        mapping = dict()
        mapping[2] = ['a','b','c']
        mapping[3] = ['d','e','f']
        mapping[4] = ['g','h','i']
        mapping[5] = ['j','k','l']
        mapping[6] = ['m','n','o']
        mapping[7] = ['p','q','r','s']
        mapping[8] = ['t','u','v']
        mapping[9] = ['w','x','y','z']

        def getCombo(digits, res):
            if len(digits) == 0:
                return res
            curr_digit, res_digit = digits[0], digits[1:]
            if int(curr_digit) in mapping:
                res = [a+b for a in res for b in mapping[int(curr_digit)]]
            return getCombo(res_digit, res)

        res = getCombo(digits, [''])
        return res

print Solution().letterCombinations('')
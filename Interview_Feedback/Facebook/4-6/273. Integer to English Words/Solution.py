# -*- coding: utf-8 -*-
class Solution(object):
    def numberToWords(self, num):
        """
        Solution:
        Time Complexity:
        Space Complexity:
        Inspired By: https://leetcode.com/problems/integer-to-english-words/discuss/70625/My-clean-Java-solution-very-easy-to-understand
        TP:
        - Divide number by 1000
        - Using list to do the mapping
        :type num: int
        :rtype: str
        """
        if num == 0: return "Zero"
        self.less_than_twenty = ['','One','Two','Three','Four','Five','Six','Seven','Eight','Nine','Ten','Eleven','Twelve','Thirteen','Fourteen',
                            'Fifteen','Sixteen','Seventeen','Eighteen','Nineteen']
        self.ten = ['','Ten','Twenty','Thirty','Forty','Fifty','Sixty','Seventy','Eighty','Ninety']
        self.thousands = ['','Thousand','Million','Billion']
        res = ''
        i = 0
        while num > 0:
            if num % 1000 != 0:
                res = self._find_less_than_thousand(num%1000) + self.thousands[i] + " " + res
            num /= 1000
            i += 1
        return res.strip()

    def _find_less_than_thousand(self, num):
        if num == 0: return ''
        elif num < 20:
            return self.less_than_twenty[num] + " "
        elif num < 100:
            return self.ten[num/10] + " " + self._find_less_than_thousand(num%10)
        else:
            return self.less_than_twenty[num/100] + " Hundred " + self._find_less_than_thousand(num % 100)

sol = Solution()
print sol.numberToWords(50868)
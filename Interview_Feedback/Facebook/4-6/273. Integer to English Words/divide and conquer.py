# -*- coding: utf-8 -*-
class Solution(object):
    def numberToWords(self, num):
        """
        Sol: divide and conquer
        Perf: Runtime: 24 ms, faster than 85.65% / Memory Usage: 11.8 MB, less than 30.47%
        :type num: int
        :rtype: str
        """
        def one(num):
            if not num:
                return ''
            switch = {
                1:'One',
                2:'Two',
                3:'Three',
                4:'Four',
                5:'Five',
                6:'Six',
                7:'Seven',
                8:'Eight',
                9:'Nine'
            }
            return switch[num]

        def two_less_twenty(num):
            switch = {
                10:'Ten',
                11:'Eleven',
                12:'Twelve',
                13:'Thirteen',
                14:'Fourteen',
                15:'Fifteen',
                16:'Sixteen',
                17:'Seventeen',
                18:'Eighteen',
                19:'Nineteen'
            }
            return switch[num]

        def ten(num):
            switch = {
                2:'Twenty',
                3:'Thirty',
                4:'Forty',
                5:'Fifty',
                6:'Sixty',
                7:'Seventy',
                8:'Eighty',
                9:'Ninety'
            }
            return switch[num]

        def two(num):
            if not num:
                return ''
            elif num < 10:
                return one(num)
            elif num < 20:
                return two_less_twenty(num)
            else:
                _ten = num/10
                _one = num%10
                if _ten and _one:
                    return ten(num/10)+' '+one(num%10)
                elif _ten:
                    return ten(num/10)
                elif _one:
                    return one(num%10)

        def three(num):
            hundred = num / 100
            rem = num - hundred*100
            if hundred and rem:
                return one(hundred)+' Hundred '+two(rem)
            elif not hundred and rem:
                return two(rem)
            elif hundred and not rem:
                return one(hundred) + ' Hundred'

        if num == 0:
            return 'Zero'

        res = ''
        billion = num / 1000000000
        rem = num - billion*1000000000
        if billion:
            res += three(billion) + ' Billion '
        million = rem / 1000000
        rem = rem - million*1000000
        if million:
            res += three(million) + ' Million '
        thousand = rem / 1000
        rem = rem - thousand*1000
        if thousand:
            res += three(thousand) + ' Thousand '
        if rem:
            res += three(rem)
        return res.strip()

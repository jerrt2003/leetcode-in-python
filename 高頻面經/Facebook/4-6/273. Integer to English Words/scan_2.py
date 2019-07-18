# -*- coding: utf-8 -*-
class Solution(object):
    def numberToWords(self, num):
        """
        Perf: Runtime: 24 ms, faster than 77.14% / Memory Usage: 11.7 MB, less than 71.25%
        :type num: int
        :rtype: str
        """
        if num == 0:
            return 'Zero'

        def one(num):
            swtich = {
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
            return swtich[num]

        def lessThanTwenty(num):
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

        def twoDigit(num):
            if num < 10:
                return one(num)
            if num < 20:
                return lessThanTwenty(num)
            digitTen = num/10
            digitRem = num%10
            if digitTen and digitRem:
                return ten(digitTen) + ' ' + one(digitRem)
            else:
                return ten(digitTen)

        def threeDigit(num):
            hundred = num/100
            rem = num%100
            if hundred and rem:
                return one(hundred) + ' Hundred ' + twoDigit(rem)
            if hundred and not rem:
                return one(hundred) + ' Hundred'
            if not hundred and rem:
                return twoDigit(num)

        res = ''
        billion = num / 1000000000
        rem = num % 1000000000
        if billion:
            res += threeDigit(billion) + ' Billion '
        million = rem / 1000000
        rem = rem % 1000000
        if million:
            res += threeDigit(million) + ' Million '
        thousand = rem / 1000
        rem = rem % 1000
        if thousand:
            res += threeDigit(thousand) + ' Thousand '
        if rem:
            res += threeDigit(rem)

        return res.rstrip()

#assert Solution().numberToWords(123) == 'One Hundred Twenty Three'
#assert Solution().numberToWords(12345) == 'Twelve Thousand Three Hundred Forty Five'
#assert Solution().numberToWords(1234567) == 'One Million Two Hundred Thirty Four Thousand Five Hundred Sixty Seven'
#assert Solution().numberToWords(1234567891) == 'One Billion Two Hundred Thirty Four Million Five Hundred Sixty Seven Thousand Eight Hundred Ninety One'
assert Solution().numberToWords(1000) == 'One Thousand'
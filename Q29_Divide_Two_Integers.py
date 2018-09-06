import math
class Solution(object):
    INT_MAX = int(math.pow(2, 31) - 1)
    INT_MIN = -int(math.pow(2, 31))
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        positive = (dividend < 0) is (divisor < 0)
        divisor, dividend = abs(divisor), abs(dividend)
        res = 0
        while divisor <= dividend:
            _divsor = divisor
            _q = 1
            while (_divsor << 1) <= dividend:
                _divsor <<= 1
                _q <<= 1
            dividend -= _divsor
            res += _q
        if positive:
            return min(res, self.INT_MAX)
        else:
            return max(-res, self.INT_MIN)

sol = Solution()
print sol.divide(7,-3)

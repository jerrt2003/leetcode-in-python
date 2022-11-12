class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        Facebook
        Math
        Hashtable
        T:O(1) S:O(n)
        Runtime: 32 ms, faster than 15.84% of Python online submissions for Fraction to Recurring Decimal.
        Memory Usage: 13 MB, less than 13.49% of Python online submissions for Fraction to Recurring Decimal.
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        ans = ''
        if (numerator/denominator) < 0:
            ans += '-'
        numerator = abs(numerator)
        denominator = abs(denominator)
        if numerator % denominator == 0:
            return ans + str(numerator/denominator)
        ans += str(numerator/denominator) + '.'
        i = len(ans)
        remainder = dict()
        numerator %= denominator
        while numerator != 0:
            if numerator not in remainder:
                remainder[numerator] = i
            else:
                i = remainder[numerator]
                ans = ans[:i] + '(' + ans[i:] + ')'
                return ans
            numerator *= 10
            ans += str(numerator/denominator)
            numerator %= denominator
            i += 1
        return ans

# print Solution().fractionToDecimal(1, 2)
print Solution().fractionToDecimal(4, 333)
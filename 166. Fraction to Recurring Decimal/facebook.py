class Solution(object):
    def fractionToDecimal(self, a, b):
        """
        Facebook
        T:O(n) S:O(n)
        Runtime: 16 ms, faster than 90.52% of Python online submissions for Fraction to Recurring Decimal.
        Memory Usage: 12.8 MB, less than 56.90% of Python online submissions for Fraction to Recurring Decimal.
        a / b
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        ans = ''
        if a * b < 0:
            ans += '-'
        a, b = abs(a), abs(b)
        ans += str(a / b)
        rem = a % b
        if rem == 0:
            return ans
        else:
            ans += '.'

        table = dict()
        i = len(ans)

        while rem:
            if rem not in table:
                table[rem] = i
            else:
                j = table[rem]
                return ans[:j] + '(' + ans[j:] + ')'
            rem *= 10
            ans += str(rem / b)
            rem %= b
            i += 1

        return ans


class Solution(object):
    def divide(self, dividend, divisor):
        """
        Facebook
        T:O(32) S:O(1)
        Runtime: 20 ms, faster than 82.93% of Python online submissions for Divide Two Integers.
        Memory Usage: 12.7 MB, less than 44.83% of Python online submissions for Divide Two Integers.
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        if dividend == -2147483648 and divisor == -1:
            return 2147483647
        a, b, res = abs(dividend), abs(divisor), 0
        for x in range(32)[::-1]:
            if (a >> x) - b >= 0:
                res += (1 << x)
                a -= b << x

        return res if dividend * divisor > 0 else -res

print Solution().divide(123,49)

class Solution(object):
    def addDigits(self, num):
        """
        Facebook
        Recursion
        T:O(V+E) S:O(1)
        Runtime: 16 ms, faster than 91.45% of Python online submissions for Add Digits.
        Memory Usage: 12.7 MB, less than 46.32% of Python online submissions for Add Digits.
        :type num: int
        :rtype: int
        """
        ans = 0
        while num > 0:
            ans += num % 10
            num = num/10
            if num == 0 and ans > 9:
                num = ans
                ans = 0
        return ans

num = 19
print Solution().addDigits(num)
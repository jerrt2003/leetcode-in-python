class Solution(object):
    def addStrings(self, num1, num2):
        """
        Facebook
        T:O(n) S:O(n)
        Runtime: 36 ms, faster than 69.69% of Python online submissions for Add Strings.
        Memory Usage: 13.1 MB, less than 8.05% of Python online submissions for Add Strings.
        :type num1: str
        :type num2: str
        :rtype: str
        """
        num1, num2 = list(num1), list(num2)
        carry, ans = 0, []
        while num1 or num2:
            n1 = ord(num1.pop()) - ord('0') if num1 else 0
            n2 = ord(num2.pop()) - ord('0') if num2 else 0

            total = n1 + n2 + carry
            ans.append(total % 10)
            carry = total / 10

        if carry:
            ans.append(1)

        return ''.join([str(c) for c in ans[::-1]])



print Solution().addStrings("0","0")

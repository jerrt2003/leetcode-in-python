class Solution(object):
    def addStrings(self, num1, num2):
        """
        Facebook
        T:O(n) S:O(n)
        :type num1: str
        :type num2: str
        :rtype: str
        """
        ans = []
        carry = 0
        def add(num1, num2, carry):
            while num1 or num2:
                n1 = ord(num1.pop()) - ord('0') if num1 else 0
                n2 = ord(num2.pop()) - ord('0') if num2 else 0
                total = carry + n1 + n2
                ans.append(str(total % 10))
                carry = total / 10
            return carry

        num1_integer, num1_float = num1.split('.')
        num2_integer, num2_float = num2.split('.')

        diff = abs(len(num1_float) - len(num2_float))
        if len(num1_float) > len(num2_float):
            num2_float += '0' * diff
        else:
            num1_float += '0' * diff

        carry = add(list(num1_float), list(num2_float), carry)
        ans.append('.')
        carry = add(list(num1_integer), list(num2_integer), carry)
        if carry:
            ans.append('1')

        return ''.join(ans[::-1])


print Solution().addStrings('123.12','45.33')
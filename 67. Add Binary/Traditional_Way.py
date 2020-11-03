class Solution(object):
    def addBinary(self, a, b):
        """
        Facebook
        T:O(n) S:O(n)
        Runtime: 24 ms, faster than 76.41% of Python online submissions for Add Binary.
        Memory Usage: 13 MB, less than 5.43% of Python online submissions for Add Binary.
        :type a: str
        :type b: str
        :rtype: str
        """
        i = len(a) - 1
        j = len(b) - 1
        ans = []
        carry = 0
        while i > -1 and j > -1:
            total = int(a[i]) + int(b[j]) + carry
            ans.append(str(total % 2))
            carry = total / 2
            i -= 1
            j -= 1
        while i > -1:
            total = int(a[i]) + carry
            ans.append(str(total % 2))
            carry = total / 2
            i -= 1
        while j > -1:
            total = int(b[j]) + carry
            ans.append(str(total % 2))
            carry = total / 2
            j -= 1
        if carry:
            ans.append(str(1))

        return ''.join(ans[::-1])











class Solution(object):
    def addBinary(self, a, b):
        """
        Facebook
        T:O(m+n) S:O(1)
        Runtime: 16 ms, faster than 97.87% of Python online submissions for Add Binary.
        Memory Usage: 12.7 MB, less than 72.55% of Python online submissions for Add Binary.
        :type a: str
        :type b: str
        :rtype: str
        """
        x, y = int(a, 2), int(b, 2)
        while y:
            answer = x ^ y
            carry = (x & y) << 1
            x, y = answer, carry
        return bin(x)[2:]

print Solution().addBinary("1101","1001")
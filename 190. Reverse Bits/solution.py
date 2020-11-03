class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        """
        Facebook
        T:O(32) T:O(1)
        Runtime: 32 ms, faster than 15.21% of Python online submissions for Reverse Bits.
        Memory Usage: 12.6 MB, less than 93.00% of Python online submissions for Reverse Bits.
        :param n:
        :return:
        """
        ans = 0
        for i in range(32):
            ans = (ans << 1) + (n & 1)
            n >>= 1
        return ans
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
        for i in range(4):
            ans = (ans << 8) + (n & 255)
            n >>= 8
        return ans

ans = Solution().reverseBits(0x12345678)
def swap32(x):
    return (((x << 24) & 0xFF000000) |
            ((x <<  8) & 0x00FF0000) |
            ((x >>  8) & 0x0000FF00) |
            ((x >> 24) & 0x000000FF))

print ans == swap32(0x12345678)
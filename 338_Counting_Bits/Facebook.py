class Solution(object):
    def countBits(self, num):
        """
        Facebook
        T:O(n) S:O(n)
        Runtime: 80 ms, faster than 45.37% of Python online submissions for Counting Bits.
        Memory Usage: 16.9 MB, less than 13.88% of Python online submissions for Counting Bits.
        :type num: int
        :rtype: List[int]
        """
        i = 0
        ans = [0]
        if num == 0:
            return ans
        for n in range(1, num + 1):
            if n == 2 ** i:
                ans.append(1)
                i += 1
            else:
                ans.append(ans[n - 2 ** (i - 1)] + 1)
        return ans


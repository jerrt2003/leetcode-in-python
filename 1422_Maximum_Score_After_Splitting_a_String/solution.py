class Solution(object):
    def maxScore(self, s):
        """
        T: O(n) S:O(1)
        Runtime: 24 ms, faster than 89.70% of Python online submissions for Maximum Score After Splitting a String.
        Memory Usage: 12.7 MB, less than 100.00% of Python online submissions for Maximum Score After Splitting a String.
        :type s: str
        :rtype: int
        """
        l_arr, r_arr = s[0], s[1:]
        if l_arr[0] == "0":
            l = 1
        else:
            l = 0
        r = r_arr.count("1")
        res = l+r
        for i in range(1, len(s)-1):
            if s[i] == '0':
                l += 1
            elif s[i] == '1':
                r -= 1
            res = max(res, l+r)
        return res


s = "011101"
print Solution().maxScore(s)
class Solution(object):
    def countSubstrings(self, s):
        """
        :type s: str
        :rtype: int
        """
        count = 0
        for i in range(2*len(s)-1):
            left = i/2
            right = left + i%2
            while left >= 0 and right < len(s):
                if s[left] == s[right]:
                    count += 1
                    left -= 1
                    right += 1
                else:
                    break
        return count

s = 'abc'
sol = Solution()
print sol.countSubstrings(s)

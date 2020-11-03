class Solution(object):
    def validPalindrome(self, s):
        """
        Facebook
        T:O(n) S:O(n)
        Runtime: 96 ms, faster than 75.17% of Python online submissions for Valid Palindrome II.
        Memory Usage: 14.1 MB, less than 21.81% of Python online submissions for Valid Palindrome II.
        :type s: str
        :rtype: bool
        """
        l, r = 0, len(s) - 1
        while l < r:
            if s[l] == s[r]:
                l += 1
                r -= 1
            else:
                return s[l+1:r+1] == s[l+1:r+1][::-1] or s[l:r] == s[l:r][::-1]
        return True

print Solution().validPalindrome("eeccccbebaeeabebccceea")
print Solution().validPalindrome("aguokepatgbnvfqmgmlcupuufxoohdfpgjdmysgvhmvffcnqxjjxqncffvmhvgsymdjgpfdhooxfuupuculmgmqfvnbgtapekouga")
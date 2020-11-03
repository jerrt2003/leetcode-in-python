class Solution(object):
    def isPalindrome(self, s):
        """
        Facebook
        2 pointer
        T:O(n) S:O(1)
        Runtime: 40 ms, faster than 74.24% of Python online submissions for Valid Palindrome.
        Memory Usage: 13.6 MB, less than 78.77% of Python online submissions for Valid Palindrome.
        :type s: str
        :rtype: bool
        """
        l, r = 0, len(s)-1
        while l < r:
            if not s[l].isalnum():
                l += 1
                continue
            elif not s[r].isalnum():
                r -= 1
                continue
            else:
                if s[l].lower() != s[r].lower():
                    return False
                l += 1
                r -= 1
        return True


print Solution().isPalindrome("A man, a plan, a canal: Panama")
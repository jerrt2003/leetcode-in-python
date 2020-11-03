import collections


class Solution(object):
    def findAnagrams(self, s, p):
        """
        Facebook
        Sliding Window
        T:O(n) S:O(n)
        Runtime: 224 ms, faster than 25.78% of Python online submissions for Find All Anagrams in a String.
        Memory Usage: 13.9 MB, less than 26.43% of Python online submissions for Find All Anagrams in a String.
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        c_ref = collections.Counter(p)
        c_runn = collections.Counter(s[:len(p)-1])
        ans = []
        for i in range(len(p)-1, len(s)):
            c_runn[s[i]] += 1
            j = i - len(p) + 1
            if c_ref == c_runn:
                ans.append(j)
            c_runn[s[j]] -= 1
            if c_runn[s[j]] == 0:
                del c_runn[s[j]]
        return ans
print Solution().findAnagrams('abcafgcba','abc')
print Solution().findAnagrams('cbaebabacd','abc')
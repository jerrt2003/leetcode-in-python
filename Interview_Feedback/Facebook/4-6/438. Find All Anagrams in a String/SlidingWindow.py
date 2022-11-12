import collections
class Solution(object):
    def findAnagrams(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: List[int]
        """
        counter = collections.Counter(p)
        window = collections.Counter(s[:len(p) - 1])
        res = []
        for i in range(len(p) - 1, len(s)):
            window[s[i]] += 1
            if window == counter:
                res.append(i - len(p) + 1)
            window[s[i - len(p) + 1]] -= 1
            if window[s[i - len(p) + 1]] == 0:
                del window[s[i - len(p) + 1]]
        return res


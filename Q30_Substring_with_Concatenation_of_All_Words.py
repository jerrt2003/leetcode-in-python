class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if s is None or words is None:
            return None
        if len(s) == 0 or len(words) == 0:
            return 0

class Solution(object):
    def distinctEchoSubstrings(self, text):
        """
        T:O(n^2) S:O(n)
        Runtime: 7040 ms, faster than 6.15% of Python online submissions for Distinct Echo Substrings.
        Memory Usage: 16.5 MB, less than 100.00% of Python online submissions for Distinct Echo Substrings.
        :type text: str
        :rtype: int
        """
        res = set()

        def check(subStr):
            if len(subStr) % 2 == 0 and subStr[:len(subStr)//2] == subStr[len(subStr)//2:]:
                return True
            return False

        for i in range(len(text)):
            for j in range(i+1, len(text)+1):
                if check(text[i:j]):
                    res.add(text[i:j])
        
        return len(res)

print(Solution().distinctEchoSubstrings('abcabcabc'))
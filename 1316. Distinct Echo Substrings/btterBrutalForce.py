class Solution(object):
    def distinctEchoSubstrings(self, text):
        """
        T:O(n^2) S:O(n)
        Runtime: 2112 ms, faster than 83.08% of Python online submissions for Distinct Echo Substrings.
        Memory Usage: 14.6 MB, less than 100.00% of Python online submissions for Distinct Echo Substrings.
        :type text: str
        :rtype: int
        """
        ans = set()
        for i in range(len(text)-1):
            start = i+1
            end = start + (start - i)
            while end <= len(text):
                if text[i:start] == text[start:end]:
                    ans.add(text[i:start])
                start += 1
                end = start + (start -i)

        return len(ans)

print(Solution().distinctEchoSubstrings("abcabcabc"))
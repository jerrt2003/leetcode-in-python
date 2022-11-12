class Solution(object):
    def palindromePairs(self, words):
        """
        Facebook
        T:O(n*k^2) S:O((k+n)^2)
        Runtime: 616 ms, faster than 61.98% of Python online submissions for Palindrome Pairs.
        Memory Usage: 14.2 MB, less than 78.10% of Python online submissions for Palindrome Pairs.
        :type words: List[str]
        :rtype: List[List[int]]
        """
        # words = {word: i for i, word in enumerate(words)}
        # ans = []
        # for word, k in words.iteritems():
        #     n = len(word)
        #     for j in range(n+1):
        #         pre = word[:j]
        #         post = word[j:]
        #         if pre == pre[::-1]:
        #             back = post[::-1]
        #             if back in words and back != word:
        #                 ans.append([words[back],k])
        #         if post == post[::-1] and j != n:
        #             back = pre[::-1]
        #             if back in words and back != word:
        #                 ans.append([k, words[back]])
        # return ans
        words = {w:i for i, w in enumerate(words)}
        ans = []
        for w, k in words.iteritems():
            l = len(w)
            for i in range(l+1):
                pre, post = w[:i], w[i:]
                if pre == pre[::-1]:
                    back = post[::-1]
                    if back in words and back != w:
                        ans.append([words[back], k])
                if post == post[::-1] and i != l:
                    back = pre[::-1]
                    if back in words and back != w:
                        ans.append([k, words[back]])
        return ans

print Solution().palindromePairs(["abcd","dcba","lls","s","sssll"])
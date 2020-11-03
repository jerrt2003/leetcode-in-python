class Solution(object):
    def isAlienSorted(self, words, order):
        """
        Facebook
        T:O(n) S:O(n)
        Runtime: 24 ms, faster than 63.82% of Python online submissions for Verifying an Alien Dictionary.
        Memory Usage: 12.9 MB, less than 23.64% of Python online submissions for Verifying an Alien Dictionary.
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        # dics = {}
        # for i, c in enumerate(order):
        #     dics[c] = i
        #
        # def valid(w1, w2):
        #     i = 0
        #     while i < len(w1) and i < len(w2):
        #         if dics[w1[i]] < dics[w2[i]]:
        #             return True
        #         elif dics[w1[i]] > dics[w2[i]]:
        #             return False
        #         else:
        #             i += 1
        #     if len(w1) == len(w2):
        #         return True
        #     else:
        #         return i < len(w2)
        #
        # l = len(words)
        # for i in range(l - 1):
        #     if not valid(words[i], words[i + 1]):
        #         return False
        # return True
        m = {}

        def translate(w):
            tmp = []
            for c in w:
                tmp.append(m[c])
            return ''.join(tmp)

        for a, b in zip(order, "abcdefghijklmnopqrstuvwxyvz"):
            m[a] = b
        for i in range(len(words)-1):
            if translate(words[i]) > translate(words[i+1]):
                return False
        return True




print Solution().isAlienSorted(["hello","leetcode"],"hlabcdefgijkmnopqrstuvwxyz")
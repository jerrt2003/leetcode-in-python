# -*- coding: utf-8 -*-
import hash2
class Solution(object):
    def isAlienSorted(self, words, order):
        """
        Solution: translate
        Time: O(nlog(n))
        Space: O(n)
        Perf: Runtime: 32 ms, faster than 30.11% / Memory Usage: 12 MB, less than 11.05%
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        maps = dict()
        for k, v in zip(order, 'abcdefghijklmnopqrstuvxyz'):
            maps[k] = v

        def translate(input):
            _res = ''
            for w in input:
                _res += maps[w]
            return _res

        for i in xrange(len(words)):
            words[i] = translate(words[i])

        return sorted(words) == words


assert Solution().isAlienSorted(["hello","leetcode"],"hlabcdefgijkmnopqrstuvwxyz") == True
assert Solution().isAlienSorted(["apple","app"],"abcdefghijklmnopqrstuvwxyz") == False
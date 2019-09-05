# -*- coding: utf-8 -*-
class Solution(object):
    def findReplaceString(self, S, indexes, sources, targets):
        """
        T: O(nlog(n))
        S: O(n)
        Perf: Runtime: 24 ms, faster than 75.00% / Memory Usage: 11.8 MB, less than 59.85%
        :type S: str
        :type indexes: List[int]
        :type sources: List[str]
        :type targets: List[str]
        :rtype: str
        """
        mapping = zip(indexes, sources, targets)
        mapping.sort(key = lambda b: b[0])

        for start_idx, source, target in mapping[::-1]:
            end_idx = start_idx + len(source)
            if end_idx > len(S):
                continue
            if S[start_idx:end_idx] == source:
                S = S[:start_idx] + target + S[end_idx:]
        return S

S = "abcd"
indexes = [0,2]
sources = ["a","cd"]
targets = ["eee","ffff"]
assert Solution().findReplaceString(S, indexes, sources, targets) == 'eeebffff'

S = "abcd"
indexes = [0,2]
sources = ["ab","ec"]
targets = ["eee","ffff"]
assert Solution().findReplaceString(S, indexes, sources, targets) == 'eeecd'

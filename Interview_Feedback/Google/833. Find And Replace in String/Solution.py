# -*- coding: utf-8 -*-
class Solution(object):
    def findReplaceString(self, S, indexes, sources, targets):
        """
        T: O(nlog(n))
        S: O(len(indexes)*(len(sources)*len(targets)) + O(n)
        Perf: Runtime: 24 ms, faster than 78.76% / Memory Usage: 11.7 MB, less than 81.05%
        :type S: str
        :type indexes: List[int]
        :type sources: List[str]
        :type targets: List[str]
        :rtype: str
        """
        mapping = dict()
        idxToBeReplaced = []
        for i in range(len(indexes)):
            idx = indexes[i]
            if S[idx:idx+len(sources[i])] == sources[i]:
                mapping[idx] = (sources[i], targets[i])
                idxToBeReplaced.append(idx)
        idxToBeReplaced.sort()

        res = ''
        lastIdx = 0
        for idx in idxToBeReplaced:
            res += S[lastIdx:idx] + mapping[idx][1]
            lastIdx = idx + len(mapping[idx][0])

        if lastIdx < len(S):
            res += S[lastIdx:]

        return res

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

S = "abcd"
indexes = [0,2]
sources = ["abc","d"]
targets = ["eee","ffff"]
assert Solution().findReplaceString(S, indexes, sources, targets) == 'eeed'



# -*- coding: utf-8 -*-
import collections
class Solution(object):
    def alienOrder(self, words):
        """
        Sol: DFS
        Perf: Runtime: 8 ms, faster than 99.77% / Memory Usage: 11.9 MB, less than 30.00%
        T: O(V+E)
        S: O(V+E)
        :type words: List[str]
        :rtype: str
        """
        self.visit = dict()
        for word in words:
            for c in word:
                if c not in self.visit:
                    self.visit[c] = 0

        # build DAG
        self.DAG = collections.defaultdict(set)
        for i in range(len(words)-1):
            currW = words[i]
            nextW = words[i+1]
            for k in range(len(currW)):
                if currW[k] != nextW[k]:
                    if currW[k] not in self.DAG or nextW[k] not in self.DAG[currW[k]]:
                        self.DAG[currW[k]].add(nextW[k])
                    break

        self.res = []
        for key in self.visit.keys():
            if self.visit[key] == 0:
                if not self.dfs(key):
                    return ''
        self.res.reverse()
        return ''.join(self.res)

    def dfs(self, c):
        self.visit[c] = -1
        for child in self.DAG[c]:
            if self.visit[child] == -1:
                return False
            elif self.visit[child] == 0:
                if not self.dfs(child):
                    return False
        self.res.append(c)
        self.visit[c] = 1
        return True

words = ["wrt","wrf","er","ett","rftt"]
#assert Solution().alienOrder(words) == 'wertf'

words = ['z','x']
#assert Solution().alienOrder(words) == 'zx'

words = ['z','x','z']
#assert Solution().alienOrder(words) == ''

words = ["za","zb","ca","cb"]
#assert Solution().alienOrder(words) == "abzc"

words = ["wrt","wrf","er","ett","rftt","te"]
#assert Solution().alienOrder(words) == "wertf"

words = ["abc","ab"]
assert Solution().alienOrder(words) == ""
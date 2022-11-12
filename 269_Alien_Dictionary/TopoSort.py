# -*- coding: utf-8 -*-
import collections
import heapq
class Solution(object):
    def alienOrder(self, words):
        """
        Solution: Topo Sort (Kahn's Algorithm)
        Perf: Runtime: 24 ms, faster than 45.79% / Memory Usage: 11.8 MB, less than 60.00%
        T: O(V+E)
        S: O(V+E)
        :type words: List[str]
        :rtype: str
        """
        children = collections.defaultdict(set)
        degree = collections.defaultdict(int)

        for word in words:
            for c in word:
                if c not in degree:
                    degree[c] = 0

        for i in range(len(words)-1):
            currWord = words[i]
            nextWord = words[i+1]
            k = 0
            while k < min(len(currWord), len(nextWord)):
                if currWord[k] != nextWord[k]:
                    if nextWord[k] not in children[currWord[k]]:
                        children[currWord[k]].add(nextWord[k])
                        degree[nextWord[k]] += 1
                    break
                else:
                    k += 1

        res = list()
        queue = list()

        for k in degree.keys():
            if degree[k] == 0:
                #heapq.heappush(queue, k)
                queue.append(k)

        while queue:
            c = queue.pop(0)
            #c = heapq.heappop(queue)
            res.append(c)
            for child in children[c]:
                degree[child] -= 1
                if degree[child] == 0:
                    #heapq.heappush(queue, child)
                    queue.append(child)

        if len(degree) != len(res):
            return ''
        else:
            return ''.join(res)

words = [
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
]

#assert Solution().alienOrder(words) == 'wertf'

words = ['z','x']
#assert Solution().alienOrder(words) == 'zx'

words = ['z','x','z']
#assert Solution().alienOrder(words) == ''

words = ["za","zb","ca","cb"]
assert Solution().alienOrder(words) == "abzc"
# -*- coding: utf-8 -*-
import collections
class Solution(object):
    def numBusesToDestination(self, routes, S, T):
        """
        :type routes: List[List[int]]
        :type S: int
        :type T: int
        :rtype: int
        """
        busStop = collections.defaultdict(set)
        for route in routes:
            for i, j in [(k, v) for k in route for v in route]:
                if i == j:
                    continue
                busStop[i].add(j)
                busStop[j].add(i)
        res = 0
        if S == T:
            return res
        if T in busStop[S]:
            return res + 1
        visited = set([k for k in busStop[S]])
        stack = [stop for stop in busStop[S]]
        while stack:
            res += 1
            for _ in range(len(stack)):
                curr = stack.pop(0)
                if T in busStop[curr]:
                    return res + 1
                else:
                    for stop in busStop[curr]:
                        if stop not in visited:
                            stack.append(stop)
        return -1

routes = [[1,2,7],[3,6,7,4],[9,4,11]]
S = 1
T = 11
assert Solution().numBusesToDestination(routes, S, T) == 3

routes = [[7,12],[4,5,15],[6],[15,19],[9,12,13]]
S = 15
T = 12
assert Solution().numBusesToDestination(routes, S, T) == -1


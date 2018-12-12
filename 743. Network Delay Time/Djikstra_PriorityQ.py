# -*- coding: utf-8 -*-
import json
from Queue import PriorityQueue as queue
class Solution(object):
    def networkDelayTime(self, times, N, K):
        """
        Solution: Djikstra + PriorityQ
        Time Complexity:
        Space Complexity:
        Inspired By: MySELF!! + Q.505
        :type times: List[List[int]]
        :type N: int
        :type K: int
        :rtype: int
        """
        distance = dict()
        distance_from_K = [float('inf') for _ in range(N)]
        for u, v, w in times:
            if u in distance:
                distance[u].append([v, w])
            else:
                distance[u] = [[v, w]]
        distance_from_K[K-1] = 0
        q = queue()
        q.put((distance_from_K[K-1], K))
        while not q.empty():
            current_node = q.get()
            val = current_node[1]
            dist = current_node[0]
            if val not in distance:
                continue
            neighbors = distance[val]
            for k, v in neighbors:
                if v + dist < distance_from_K[k-1]:
                    distance_from_K[k-1] = v + dist
                    if k in distance:
                        q.put((distance_from_K[k-1], k))
        res = max(distance_from_K)
        return -1 if res == float('inf') else res

def stringToInt2dArray(input):
    return json.loads(input)

def stringToInt(input):
    return int(input)

def intToString(input):
    if input is None:
        input = 0
    return str(input)

#times = [(1,2,1),(2,3,1),(3,4,1)]
#N = 4
#K = 1
#times = [[1,2,1]]
#N = 2
#K = 2

ret = Solution().networkDelayTime(times, N, K)

out = intToString(ret)
print out
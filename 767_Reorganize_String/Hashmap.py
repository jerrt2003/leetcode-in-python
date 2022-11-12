# -*- coding: utf-8 -*-
import collections
import heapq
class Solution(object):
    def reorganizeString(self, S):
        """
        Sol: Hashmap + heapq
        Perf: Runtime: 24 ms, faster than 43.37% / Memory Usage: 11.9 MB, less than 20.00%
        T: O(n + nlog(n) + n + nlog(n))
        S: O(n)
        :type S: str
        :rtype: str
        """
        counter = collections.Counter(S)
        res = ''
        pq = []
        for k, v in counter.iteritems():
            heapq.heappush(pq, (-v, k))
        lenS = len(S)
        while lenS > 0:
            count, c = heapq.heappop(pq)
            if len(res) == 0 or c != res[-1]:
                res += c
                count += 1
                if count != 0:
                    heapq.heappush(pq, (count, c))
            else:
                if pq:
                    count2, c2 = heapq.heappop(pq)
                    res += c2
                    count2 += 1
                    if count2 != 0:
                        heapq.heappush(pq, (count2, c2))
                    heapq.heappush(pq, (count, c))
                else:
                    return ''
            lenS -= 1
        return res

#assert Solution().reorganizeString('aab') == 'aba'
assert Solution().reorganizeString('vvvlo') == 'vlvov'
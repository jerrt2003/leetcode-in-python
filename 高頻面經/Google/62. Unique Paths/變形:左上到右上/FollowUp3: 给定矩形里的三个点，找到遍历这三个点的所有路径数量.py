# -*- coding: utf-8 -*-
import hash2
class Solution(object):
    def uniquePath(self, m, n, cords):
        cords.sort(key=lambda cord: cord[0])
        final_i = cords[-1][0]
        preCheck = hash2.defaultdict(list)
        for i, j in cords:
            preCheck[j].append(i)
            if len(preCheck[j]) > 1:
                return False
        DP = [0 for _ in range(m)]
        for j in range(n):
            tmp = DP[:]
            for i in range(m):
                if i == 0 and j == 0:
                    DP[i] = 1
                    continue
                val1 = tmp[i-1] if i-1 >= 0 and j-1 >= 0 else 0
                val2 = tmp[i] if j-1 >= 0 else 0
                val3 = tmp[i+1] if i+1 < m and j-1 >= 0 else 0
                DP[i] = val1+val2+val3
            if j in preCheck:
                i = preCheck[j][0]
                for idx in range(len(DP)):
                    if idx != i:
                        DP[idx] = 0
        return DP[final_i]

assert Solution().uniquePath(3, 4, [(0,0),(1,2),(2,3)]) == 2
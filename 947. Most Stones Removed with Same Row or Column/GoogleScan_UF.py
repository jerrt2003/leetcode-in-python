# -*- coding: utf-8 -*-
class Solution(object):
    def removeStones(self, stones):
        """
        Solution: Union Find
        Time Complexity: O(nlog(n))
        Space Complexity: O(n)
        Perf: Runtime: 296 ms, faster than 42.72% / Memory Usage: 12.4 MB, less than 28.77%
        :type stones: List[List[int]]
        :rtype: int
        """
        UF = UnionFind(stones)
        for i, j in stones:
            UF.union(i, j+10000)
        disjoin_set = set()
        for i, j in stones:
            r = UF.find(j+10000)
            if r not in disjoin_set:
                disjoin_set.add(r)
        return len(stones) - len(disjoin_set)

class UnionFind(object):
    def __init__(self, stones):
        self.UF = {}
        for i, j in stones:
            self.UF[i] = i
            self.UF[j+10000] = j+10000

    def find(self, x):
        if x != self.UF[x]:
            self.UF[x] = self.find(self.UF[x])
        return self.UF[x]

    def union(self, i, j):
        r1 = self.find(i)
        r2 = self.find(j)
        if r1 != r2:
            self.UF[r1] = r2


#stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
#stones = [[0,0],[0,2],[1,1],[2,0],[2,2]]
#stones = [[0,0]]
stones = [[1,2],[1,3],[3,3],[3,1],[2,1],[1,0]]
print Solution().removeStones(stones)
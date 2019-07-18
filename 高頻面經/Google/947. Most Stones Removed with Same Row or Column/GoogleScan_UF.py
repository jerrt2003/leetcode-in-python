class Solution(object):
    def removeStones(self, stones):
        """
        :type stones: List[List[int]]
        :rtype: int
        """
        N = len(stones)
        uf = UnionFind(20000)
        for i, j in stones:
            uf.union(i, j + 10000)
        island = set()
        for i, j in stones:
            r = uf.find(i)
            if r not in island:
                island.add(r)
        return N - len(island)


class UnionFind(object):
    def __init__(self, N):
        self.p = [i for i in range(N)]

    def find(self, pt):
        if self.p[pt] != pt:
            self.p[pt] = self.find(self.p[pt])
        return self.p[pt]

    def union(self, p1, p2):
        r1 = self.find(p1)
        r2 = self.find(p2)
        if r1 != r2:
            self.p[r2] = r1
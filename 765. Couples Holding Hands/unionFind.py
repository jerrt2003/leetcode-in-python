class Solution(object):
    def minSwapsCouples(self, row):
        """
        O(n) S:O(n)
        Runtime: 16 ms, faster than 93.75% of Python online submissions for Couples Holding Hands.
        Memory Usage: 12.8 MB, less than 40.40% of Python online submissions for Couples Holding Hands.
        https://leetcode.com/problems/couples-holding-hands/discuss/117520/Java-union-find-easy-to-understand-5-ms
        :type row: List[int]
        :rtype: int
        """
        N = len(row)/2
        uf = UnionFind(N)
        for i in range(N):
            uf.union(row[2*i]/2, row[2*i+1]/2)
        return N - uf.count

class UnionFind(object):
    def __init__(self, N):
        self.parent = [i for i in range(N)]
        self.count = N

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, i, j):
        ri = self.find(i)
        rj = self.find(j)
        if ri != rj:
            self.parent[rj] = ri
            self.count -= 1
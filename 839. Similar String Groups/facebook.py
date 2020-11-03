class Solution(object):
    def numSimilarGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """

        def isSimilar(s1, s2):
            if s1 == s2:
                return True
            i = 0
            while i < len(s1):
                if s1[i] != s2[i]:
                    break
                i += 1
            arrS1 = [c for c in s1]
            arrS2 = [c for c in s2]
            for j in range(i + 1, len(s1)):
                if arrS1[j] == arrS2[i]:
                    arrS1[i], arrS1[j] = arrS1[j], arrS1[i]
                    if arrS1 == arrS2:
                        return True
                    arrS1[i], arrS1[j] = arrS1[j], arrS1[i]
            return False

        uf = UnionFind(len(A))

        for i in range(len(A) - 1):
            for j in range(1, len(A)):
                if isSimilar(A[i], A[j]):
                    uf.union(i, j)

        return uf.count


class UnionFind(object):
    def __init__(self, N):
        self.parent = range(N)
        self.count = N

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        rx = self.find(x)
        ry = self.find(y)
        if rx != ry:
            self.parent[ry] = rx
            self.count -= 1


print Solution().numSimilarGroups(["tars","rats","arts","star"])
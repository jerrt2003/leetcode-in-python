class Solution(object):
    def numSimilarGroups(self, A):
        """
        :type A: List[str]
        :rtype: int
        """
        uf = UnionFind(A)
        def isSimilar(str_a, str_b):
            # if str_a == str_b:
            #     return True
            # i = 0
            # while str_a[i] == str_b[i]:
            #     i += 1
            # for j in range(i+1, len(str_a)):
            #     if str_a[j] == str_b[i]:
            #         if str_a[:i]+str_a[j]+str_a[i+1:j]+str_a[i]+str_a[j+1:] == str_b:
            #             return True
            # return False
            i, diff = 0, 0
            while i < len(str_a):
                if str_a[i] != str_b[i]:
                    diff += 1
                    if diff > 2:
                        return False
                i += 1
            return True

        for i in range(len(A)-1):
            for j in range(i+1, len(A)):
                if isSimilar(A[i],A[j]):
                    uf.union(i, j)

        return uf.count

class UnionFind(object):
    def __init__(self, A):
        self.parent = [i for i in range(len(A))]
        self.count = len(A)

    def union(self, i, j):
        root_i = self.find(i)
        root_j = self.find(j)
        if root_i != root_j:
            self.parent[root_j] = root_i
            self.count -= 1

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]


print Solution().numSimilarGroups(["tars","rats","arts","star"])
print Solution().numSimilarGroups(["abc","abc"])
print Solution().numSimilarGroups(["koqnn","knnqo","noqnk","nqkon"])
print Solution().numSimilarGroups(["abc","abc","abc"])
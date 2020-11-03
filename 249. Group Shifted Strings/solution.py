import collections


class Solution(object):
    def groupStrings(self, strings):
        """
        :type strings: List[str]
        :rtype: List[List[str]]
        """

        def test(str1, str2):
            if len(str1) != len(str2):
                return False
            diff = (26 + ord(str1[0]) - ord(str2[0])) % 26
            for c1, c2 in zip(str1[1:], str2[1:]):
                if (26 + ord(c1) - ord(c2)) % 26 != diff:
                    return False
            return True

        n = len(strings)
        uf = UnionFind(n)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if test(strings[i], strings[j]):
                    uf.union(i, j)
        ans = collections.defaultdict(list)
        for k, v in enumerate(uf.parent):
            ans[v].append(strings[k])

        return ans.values()


class UnionFind(object):
    def __init__(self, n):
        self.parent = range(n)

    def find(self, x):
        if self.parent[x] != x:
            self.parent[x] = self.find(self.parent[x])
        return self.parent[x]

    def union(self, x, y):
        r_x = self.find(x)
        r_y = self.find(y)
        if r_x != r_y:
            self.parent[r_y] = r_x


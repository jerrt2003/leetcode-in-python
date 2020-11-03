import collections


class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        uf = UnionFind(accounts)
        for group in uf.grouping:
            for a, b in zip(group[:len(group) - 1], group[1:]):
                uf.union(a, b)

        table = collections.defaultdict(list)
        for k, v in uf.parent.iteritems():
            table[v].append(k)

        ans = []
        for k, v in table.iteritems():
            ans.append([uf.name2emails[k]] + sorted(v))

        return ans


class UnionFind(object):
    def __init__(self, accounts):
        self.name2emails = collections.defaultdict(str)
        self.parent = collections.defaultdict(str)
        self.grouping = []

        for i in range(len(accounts)):
            name, emails = accounts[i][0], accounts[i][1:]
            for email in emails:
                self.parent[email] = email
                self.name2emails[email] = name
            self.grouping.append(emails)

    def find(self, a):
        if self.parent[a] != a:
            self.parent[a] = self.find(self.parent[a])
        return self.parent[a]

    def union(self, a, b):
        r_a = self.find(a)
        r_b = self.find(b)
        if r_a != r_b:
            self.parent[b] = r_a

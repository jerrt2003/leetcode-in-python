# -*- coding: utf-8 -*-
import hash2
class Solution(object):
    def accountsMerge(self, accounts):
        """
        Sol: UnionFind
        Time Complexity: O(nlog(n))
        Space Complexity: O(n)
        Perf: Runtime: 248 ms, faster than 48.83% / Memory Usage: 18.5 MB, less than 48.19%
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        emToName = {}
        emToId = {}
        idToEm = {}
        id = 0
        uf = UnionFind(10001)
        for account in accounts:
            _name = account[0]
            _emails = account[1:]
            for _email in _emails:
                emToName[_email] = _name
                if _email not in emToId:
                    emToId[_email] = id
                    idToEm[id] = _email
                    id += 1
                uf.union(emToId[_emails[0]], emToId[_email])
        _ans = hash2.defaultdict(list)
        for _email in emToId:
            _ans[uf.find(emToId[_email])].append(_email)
        ans = []
        for k, v in _ans.iteritems():
            ans.append([emToName[idToEm[k]]]+sorted(v))
        return ans

class UnionFind(object):
    def __init__(self, count):
        self.parent = [i for i in range(count)]

    def find(self, id):
        if id != self.parent[id]:
            self.parent[id] = self.find(self.parent[id])
        return self.parent[id]

    def union(self,id1,id2):
        r1 = self.find(id1)
        r2 = self.find(id2)
        if r1!= r2:
            self.parent[r2] = r1

#assert Solution().accountsMerge([["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]])
assert Solution().accountsMerge([["David","David0@m.co","David4@m.co","David3@m.co"],["David","David5@m.co","David5@m.co","David0@m.co"],["David","David1@m.co","David4@m.co","David0@m.co"],["David","David0@m.co","David1@m.co","David3@m.co"],["David","David4@m.co","David1@m.co","David3@m.co"]])
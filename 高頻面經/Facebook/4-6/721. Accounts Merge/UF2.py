# -*- coding: utf-8 -*-
import collections
class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        uf = UnionFind(10001)
        em_to_id = dict()
        id_to_em = dict()
        em_to_name = dict()
        id = 0
        for acct in accounts:
            name = acct[0]
            emails = acct[1:]
            for em in emails:
                em_to_name[em] = name
                if em not in em_to_id:
                    em_to_id[em] = id
                    id_to_em[id] = em
                    id += 1
                uf.union(em_to_id[emails[0]], em_to_id[em])
        group = collections.defaultdict(list)
        for em in em_to_id:
            group[uf.find(em_to_id[em])].append(em)
        res = []
        for k, v in group.iteritems():
            res.append([em_to_name[id_to_em[k]]] + sorted(v))
        return res

class UnionFind(object):
    def __init__(self, count):
        self.parent = [i for i in range(count)]

    def find(self, id):
        if self.parent[id] != id:
            self.parent[id] = self.find(self.parent[id])
        return self.parent[id]

    def union(self, id1, id2):
        r1 = self.find(id1)
        r2 = self.find(id2)
        if r1 != r2:
            self.parent[r2] = r1
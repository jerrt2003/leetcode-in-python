# -*- coding: utf-8 -*-
import hash2
class Solution(object):
    def accountsMerge(self, accounts):
        """
        Draw an edge between two emails if they occur in the same account. The problem comes down to finding connected components of this graph.
        Perf: Runtime: 672 ms, faster than 12.89% / Memory Usage: 18.9 MB, less than 42.57%
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        em_to_name = {}
        em_maps = hash2.defaultdict(list)
        for acct in accounts:
            name = acct[0]
            emails = acct[1:]
            for em in emails:
                if em not in em_to_name:
                    em_to_name[em] = name
                for _tmp in emails:
                    if _tmp not in em_maps[em]:
                        em_maps[em].append(_tmp)
        visited = set()
        ans = []
        for key in em_maps.keys():
            if key not in visited:
                _res = []
                stack = [key]
                while stack:
                    curr = stack.pop(0)
                    _res.append(curr)
                    visited.add(curr)
                    for nb in em_maps[curr]:
                        if nb not in visited and nb not in stack:
                            stack.append(nb)
                ans.append([em_to_name[key]]+sorted(_res))
        return ans

#assert Solution().accountsMerge([["David","David0@m.co","David4@m.co","David3@m.co"],["David","David5@m.co","David5@m.co","David0@m.co"],["David","David1@m.co","David4@m.co","David0@m.co"],["David","David0@m.co","David1@m.co","David3@m.co"],["David","David4@m.co","David1@m.co","David3@m.co"]])
assert Solution().accountsMerge([["John","johnsmith@mail.com","john_newyork@mail.com"],["John","johnsmith@mail.com","john00@mail.com"],["Mary","mary@mail.com"],["John","johnnybravo@mail.com"]])
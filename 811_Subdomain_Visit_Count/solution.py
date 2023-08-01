import collections
from typing import List


class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        domain_visit_count = collections.defaultdict(int)
        for cpdomain in cpdomains:
            count, domain = cpdomain.split(" ")
            count = int(count)
            domain = domain.split(".")[::-1]
            for i in range(len(domain)):
                visit_domain = ""
                for j in range(i + 1):
                    visit_domain = domain[j] + "." + visit_domain
                visit_domain = visit_domain[:-1]
                domain_visit_count[visit_domain] += count

        ans = []
        for subdomain, count in domain_visit_count.items():
            count_domain_pair = str(count) + " " + subdomain
            ans.append(count_domain_pair)

        return ans

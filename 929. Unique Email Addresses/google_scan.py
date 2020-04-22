# -*- coding: utf-8 -*-
import collections
class Solution(object):
    def numUniqueEmails(self, emails):
        """
        Solution: O(n)
        Time Complexity: O(n)
        Space Complexity: O(n)
        Inspired By: MySELF!!
        Perf: Runtime: 32 ms, faster than 95.04% / Memory Usage: 11 MB, less than 9.52%
        :type emails: List[str]
        :rtype: int
        """
        res = collections.defaultdict(int)
        for email in emails:
            localname, domainname = email.split('@')
            localname = localname.split('+')[0]
            localname = localname.replace('.','')
            res[localname+'@'+domainname] += 1
        return len(res.keys())
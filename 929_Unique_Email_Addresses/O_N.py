# -*- coding: utf-8 -*-
class Solution(object):
    def numUniqueEmails(self, emails):
        """
        Solution: SET
        Time Complexity: O(n)
        Space Complexity: O(n)
        Inspired By: MySELF!! (60ms, beat 33.76%)
        TP:
        - Using SET to de-dup
        :type emails: List[str]
        :rtype: int
        """
        res = set()

        def _analyzeEmail(email):
            split_res = email.split('@')
            if len(split_res) != 2:
                return # invalid email
            local = split_res[0]
            domain = split_res[1]
            local = ''.join(local.split('.'))
            local = local.split('+')[0]
            key = local + domain
            res.add(key)

        for email in emails:
            _analyzeEmail(email)

        return len(res)

emails = ["test.abc.email+alex@leetcode.com","test.e.mail+bob.cathy@leetcode.com","testemail+david@lee.tcode.com"]

print Solution().numUniqueEmails(emails)
# -*- coding: utf-8 -*-
import collections
import bisect
class Solution(object):

    """
    Question:
    source: ‘abc’. subsequences: a,b,c,ab,ac,bc,abc target: ‘abcac’
    Can the target string be constructed by concatenating the subsequences of the source string?
    follow up: What is the minimum number of concatenations required?

    Time Complexity: O(nlog(n))
    Space Complexity: O(n)
    """

    def constructCount(self, src, dst):
        pos_dict = collections.defaultdict(list)
        for i, c in enumerate(src):
            pos_dict[c].append(i)

        last_idx = -float('inf')
        count = 1
        for c in dst:
            if c not in pos_dict:
                return 0
            pos = bisect.bisect_left(pos_dict[c], last_idx+1)
            if pos == len(pos_dict[c]):
                count += 1
                last_idx = pos_dict[c][0]
            else:
                last_idx = pos_dict[c][pos]
        return count


src = "bcaecbcd"
aim = "dcbceacb"
print(Solution().constructCount(src, aim))

src = 'abcdb'
aim = 'ba'
print(Solution().constructCount(src, aim))

src = 'abcadb'
aim = 'aaaa'
print(Solution().constructCount(src, aim))

src = "aabaaaaabaaabbbbaaaa"
aim = "bbaabbbb"
print(Solution().constructCount(src, aim))

# -*- coding: utf-8 -*-
import hash2
class Solution(object):
    def totalFruit(self, tree):
        """
        Solution: Sliding Window + 2-pointer
        Time complexity: O(n)
        Space Complexity: O(1)
        Perf: Runtime: 408 ms, faster than 31.46% / Memory Usage: 14.4 MB, less than 34.35%
        Inspired By: MySELF!!
        :type tree: List[int]
        :rtype: int
        """
        if not tree: return 0
        m = len(tree)
        bskt = hash2.defaultdict(int)
        pt1, pt2 = 0, 1
        bskt[tree[pt1]] = 1
        res = 1
        while pt2 < m:
            bskt[tree[pt2]] += 1
            while len(bskt.keys()) > 2:
                bskt[tree[pt1]] -= 1
                if bskt[tree[pt1]] == 0:
                    del bskt[tree[pt1]]
                pt1 += 1
            res = max(res, pt2-pt1+1)
            pt2 += 1
        return res

tree = []
print Solution().totalFruit(tree)
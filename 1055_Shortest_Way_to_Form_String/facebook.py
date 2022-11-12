import collections


class Solution(object):
    def shortestWay(self, source, target):
        """
        Facebook
        T:O(nlogn) S:O(n)
        Runtime: 44 ms, faster than 65.36% of Python online submissions for Shortest Way to Form String.
        Memory Usage: 12.9 MB, less than 25.14% of Python online submissions for Shortest Way to Form String.
        :type source: str
        :type target: str
        :rtype: int
        """
        charPos = collections.defaultdict(list)
        for i, c in enumerate(source):
            charPos[c].append(i)

        def findNextIdx(idx, c):
            lst = charPos[c]
            l, r = 0, len(charPos[c])
            while l < r:
                m = (l + r - 1) / 2
                if lst[m] > idx:
                    r = m
                else:
                    l = m + 1
            return l

        cnt = 1
        idx = -1
        for c in target:
            if c not in charPos:
                return -1
            pos = findNextIdx(idx, c)
            if pos == len(charPos[c]):
                cnt += 1
                idx = charPos[c][0]
            else:
                idx = charPos[c][pos]

        return cnt

print Solution().shortestWay("xyz","xzyxz")
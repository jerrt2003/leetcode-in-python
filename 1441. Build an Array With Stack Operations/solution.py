class Solution(object):
    def buildArray(self, target, n):
        """
        2 pointer + stack
        T:O(n) S:O(1)
        Runtime: 8 ms, faster than 99.76% of Python online submissions for Build an Array With Stack Operations.
        Memory Usage: 12.8 MB, less than 100.00% of Python online submissions for Build an Array With Stack Operations.
        :type target: List[int]
        :type n: int
        :rtype: List[str]
        """
        ret = []
        i = 0
        n = 1
        while i < len(target):
            if target[i] != n:
                ret.append("Push")
                ret.append("Pop")
            else:
                ret.append("Push")
                i += 1
            n += 1
        return ret

print Solution().buildArray([1,3], 3)
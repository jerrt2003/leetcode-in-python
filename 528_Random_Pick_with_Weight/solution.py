from random import random


class Solution(object):

    def __init__(self, w):
        """
        Facebook
        T:O(n)
        :type w: List[int]
        """
        self.sum_w = 0
        self.prefix = []
        for i, v in enumerate(w):
            self.sum_w += v
            self.prefix.append([i, self.sum_w])

    def pickIndex(self):
        """
        T:O(log(n))
        :rtype: int
        """
        idx = random.randint(1, self.sum_w)
        l, r = 0, len(self.prefix)
        while l < r:
            m = (l + r - 1) / 2
            if self.prefix[m][1] >= idx:
                r = m
            else:
                l = m + 1
        return self.prefix[l][0]

# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
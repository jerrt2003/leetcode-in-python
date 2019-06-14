# -*- coding: utf-8 -*-
import random
class Solution(object):

    def __init__(self, w):
        """
        Solution: BS
        Time: O(n) for init, O(log(n)) for pickIndex
        Space: O(n)
        :type w: List[int]
        """
        self.weight = []
        for _w in w:
            if not self.weight:
                self.weight.append(_w)
            else:
                self.weight.append(_w + self.weight[-1])

    def pickIndex(self):
        """a
        :rtype: int
        """
        target = random.randint(0, self.weight[-1] - 1)
        l, r = 0, len(self.weight)
        while l < r:
            mid = (l + r - 1) // 2
            if target < self.weight[mid]:
                r = mid
            else:
                l = mid + 1
        return l


# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()
# Your Solution object will be instantiated and called as such:
# obj = Solution(w)
# param_1 = obj.pickIndex()

sol = Solution([1,2,3,4])
print sol.pickIndex()
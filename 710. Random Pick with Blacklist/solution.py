from random import randint


class Solution(object):

    def __init__(self, N, blacklist):
        """
        Binary Search
        :type N: int
        :type blacklist: List[int]
        """
        self.blacklist = sorted(blacklist)
        self.pool = N - len(blacklist)


    def pick(self):
        """
        :rtype: int
        """
        k = randint(0,self.pool)
        l, r = 0, len(self.blacklist)
        while l < r:
            mid = (l+r-1)/2
            if self.blacklist[mid] - mid > k:
                r = mid
            else:
                l = mid+1
        return k+l if l == len(self.blacklist) else k+(l-1)+1







# Your Solution object will be instantiated and called as such:
# obj = Solution(N, blacklist)
# param_1 = obj.pick()
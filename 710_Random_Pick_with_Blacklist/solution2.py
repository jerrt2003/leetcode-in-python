from random import randint


class Solution(object):

    def __init__(self, N, blacklist):
        """
        Virtual Whitelist
        T:O(n) S:O(len(blacklist))
        Runtime: 380 ms, faster than 67.95% of Python online submissions for Random Pick with Blacklist.
        Memory Usage: 21.9 MB, less than 100.00% of Python online submissions for Random Pick with Blacklist.
        :type N: int
        :type blacklist: List[int]
        """
        self.mapping = dict()
        for b in blacklist:
            self.mapping[b] = -1
        self.M = N - len(blacklist)
        for b in blacklist:
            if b < self.M:
                while N-1 in self.mapping:
                    N -= 1
                self.mapping[b] = N-1
                N -= 1


    def pick(self):
        """
        T:O(1)
        :rtype: int
        """
        rand_int = randint(0, self.M-1)
        if rand_int in self.mapping:
            return self.mapping[rand_int]
        return rand_int


# Your Solution object will be instantiated and called as such:
# obj = Solution(N, blacklist)
# param_1 = obj.pick()
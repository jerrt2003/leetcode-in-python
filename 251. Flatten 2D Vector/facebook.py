class Vector2D(object):

    def __init__(self, v):
        """
        Facebook
        T:O(V/N) S:O(1)
        Runtime: 80 ms, faster than 73.57% of Python online submissions for Flatten 2D Vector.
        Memory Usage: 19.1 MB, less than 92.14% of Python online submissions for Flatten 2D Vector.
        :type v: List[List[int]]
        """
        self.inner = 0
        self.outer = 0
        self.v = v

    def advance(self):
        while self.outer < len(self.v) and self.inner == len(self.v[self.outer]):
            self.outer += 1
            self.inner = 0

    def next(self):
        """
        T:O(V/N)
        :rtype: int
        """
        self.advance()
        ret = self.v[self.outer][self.inner]
        self.inner += 1
        return ret

    def hasNext(self):
        """
        T:O(V/N)
        :rtype: bool
        """
        self.advance()
        return self.outer < len(self.v)

# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(v)
# param_1 = obj.next()
# param_2 = obj.hasNext()
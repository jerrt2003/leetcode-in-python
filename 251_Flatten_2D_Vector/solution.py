class Vector2D(object):

    def __init__(self, v):
        """
        T:O(n) S:O(n)
        :type v: List[List[int]]
        """
        self.stack = []
        for _v in v[::-1]:
            if len(_v) > 0:
                self.stack.append(_v)

    def next(self):
        """
        T:O(1)
        :rtype: int
        """
        curr = self.stack.pop()
        if len(curr) < 2:
            return curr[0]
        else:
            self.stack.append(curr[1:])
            return curr[0]

    def hasNext(self):
        """
        T:O(1)
        :rtype: bool
        """
        return True if len(self.stack) != 0 else False

# Your Vector2D object will be instantiated and called as such:
# obj = Vector2D(v)
# param_1 = obj.next()
# param_2 = obj.hasNext()
class CombinationIterator(object):

    def __init__(self, characters, combinationLength):
        """
        Backtracking
        T:O(V+E) S:O(V+E)
        Runtime: 44 ms, faster than 69.81% of Python online submissions for Iterator for Combination.
        Memory Usage: 15.7 MB, less than 100.00% of Python online submissions for Iterator for Combination.
        :type characters: str
        :type combinationLength: int
        """
        self.combo = []
        def dfs(path, remaining, idx):
            if remaining == 0:
                self.combo.append(path)
                return
            for nexIdx in range(idx, len(characters)):
                dfs(path+characters[nexIdx], remaining-1, nexIdx+1)

        for i in range(len(characters)):
            dfs(characters[i], combinationLength-1, i+1)
        self.iter = 0

    def next(self):
        """
        :rtype: str
        """
        ret = self.combo[self.iter]
        self.iter += 1
        return ret


    def hasNext(self):
        """
        :rtype: bool
        """
        if self.iter < len(self.combo):
            return True
        return False

# Your CombinationIterator object will be instantiated and called as such:
# obj = CombinationIterator(characters, combinationLength)
# param_1 = obj.next()
# param_2 = obj.hasNext()

sol = CombinationIterator('gkosu', 3)
sol.next()
sol.hasNext()
sol.next()
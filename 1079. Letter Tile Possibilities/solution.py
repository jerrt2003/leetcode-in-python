import collections


class Solution(object):
    def numTilePossibilities(self, tiles):
        """
        Backtracking
        Runtime: 136 ms, faster than 39.82% of Python online submissions for Letter Tile Possibilities.
        Memory Usage: 22.9 MB, less than 7.06% of Python online submissions for Letter Tile Possibilities.
        :type tiles: str
        :rtype: int
        """
        # self.visit = set()
        # def backTrack(path, options):
        #     if path and path not in self.visit:
        #         self.visit.add(path)
        #     for k in options:
        #         if options[k] != 0:
        #             options[k] -= 1
        #             backTrack(path + k, options)
        #             options[k] += 1
        #
        # counter = collections.Counter(tiles)
        # backTrack('',counter)
        # return len(self.visit)
        res = set()
        def dfs(path, t):
            if path:
                res.add(path)
            for i in range(len(t)):
                dfs(path+t[i], t[:i]+t[i+1:])
        dfs('', tiles)
        return len(res)

print Solution().numTilePossibilities("AAB")
print Solution().numTilePossibilities("AAABBC")
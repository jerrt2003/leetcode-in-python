class Solution(object):
    def peopleIndexes(self, favoriteCompanies):
        """
        T:O(log*n) S:O(n)
        Runtime: 380 ms, faster than 85.58% of Python online submissions for People Whose List of Favorite Companies Is Not a Subset of Another List.
        Memory Usage: 29.9 MB, less than 100.00% of Python online submissions for People Whose List of Favorite Companies Is Not a Subset of Another List.
        :type favoriteCompanies: List[List[str]]
        :rtype: List[int]
        """
        l = len(favoriteCompanies)
        self.parent = [i for i in range(l)]
        for i in range(l):
            for j in range(i+1, l):
                root_i = self.find(i)
                root_j = self.find(j)
                if root_i == root_j:
                    continue
                elif self.contain(favoriteCompanies[i], favoriteCompanies[j]):
                    self.parent[j] = root_i
                elif self.contain(favoriteCompanies[j], favoriteCompanies[i]):
                    self.parent[i] = root_j
        return [i for i in range(l) if self.parent[i] == i]   

    def find(self, i):
        if self.parent[i] != i:
            self.parent[i] = self.parent[self.parent[i]]
        return self.parent[i]

    def contain(self, a, b):
        """
        check if b is containing in a
        """
        if len(a) <= len(b):
            return False
        set_a = set(a)
        for char in b:
            if char not in set_a:
                return False
        return True


# print(Solution().peopleIndexes([["leetcode","google","facebook"],["google","microsoft"],["google","facebook"],["google"],["amazon"]]))
print(Solution().peopleIndexes([["leetcode","google","facebook"],["leetcode","amazon"],["facebook","google"]]))
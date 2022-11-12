class Solution(object):
    def peopleIndexes(self, favoriteCompanies):
        """
        T:O(n^2) S:O(n)
        Runtime: 864 ms, faster than 39.57% of Python online submissions for People Whose List of Favorite Companies Is Not a Subset of Another List.
        Memory Usage: 29.8 MB, less than 100.00% of Python online submissions for People Whose List of Favorite Companies Is Not a Subset of Another List.
        :type favoriteCompanies: List[List[str]]
        :rtype: List[int]
        """
        ans = []
        for i in range(len(favoriteCompanies)):
            isSubtset = False
            for j in range(len(favoriteCompanies)):
                if i != j:
                    if set(favoriteCompanies[i]).issubset(set(favoriteCompanies[j])):
                        isSubtset = True
                        break
            if not isSubtset:
                ans.append(i)
        return ans

print(Solution().peopleIndexes([["leetcode","google","facebook"],["google","microsoft"],["google","facebook"],["google"],["amazon"]]))


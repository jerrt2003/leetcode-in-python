class Solution(object):
    def letterCombinations(self, digits):
        """
        T:O(V+E) S:O(V+E)
        Runtime: 20 ms, faster than 63.58% of Python online submissions for Letter Combinations of a Phone Number.
        Memory Usage: 12.9 MB, less than 25.86% of Python online submissions for Letter Combinations of a Phone Number.
        :type digits: str
        :rtype: List[str]
        """
        num2chr = dict()
        num2chr['1'] = ['']
        num2chr['2'] = ['a', 'b', 'c']
        num2chr['3'] = ['d', 'e', 'f']
        num2chr['4'] = ['g', 'h', 'i']
        num2chr['5'] = ['j', 'k', 'l']
        num2chr['6'] = ['m', 'n', 'o']
        num2chr['7'] = ['p', 'q', 'r', 's']
        num2chr['8'] = ['t', 'u', 'v']
        num2chr['9'] = ['w', 'x', 'y', 'z']
        num2chr['0'] = ['']

        def dfs(i, path):
            if i == len(digits):
                return path
            path = [a + b for a in path for b in num2chr[digits[i]]]
            return dfs(i + 1, path)

        if len(digits) == 0:
            return []
        return dfs(0, [''])
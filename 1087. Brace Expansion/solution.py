class Solution(object):
    def expand(self, S):
        """
        T:O(n) S:O(n)
        Runtime: 24 ms, faster than 88.35% of Python online submissions for Brace Expansion.
        Memory Usage: 12.9 MB, less than 58.72% of Python online submissions for Brace Expansion.
        :type S: str
        :rtype: List[str]
        """
        def helper(i):
            cache = ''
            while i < len(S):
                if S[i] == '}':
                    return i, cache.split(',')
                cache += S[i]
                i += 1

        k = 0
        res = ['']
        while k < len(S):
            if S[k] == '{':
                k, tmp = helper(k+1)
                res = [a + b for a in res for b in tmp]
            else:
                res = [a + S[k] for a in res]
            k += 1

        return sorted(res)



# print Solution().expand("{a,b}c{d,e}f")
# print Solution().expand("abcd")
print Solution().expand("{a,b}{z,x,y}")
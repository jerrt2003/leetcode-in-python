class Solution(object):
    def kSimilarity(self, A, B):
        """
        Runtime: 512 ms, faster than 35.42% of Python online submissions for K-Similar Strings.
        Memory Usage: 22.3 MB, less than 50.68% of Python online submissions for K-Similar Strings.
        https://leetcode.com/problems/k-similar-strings/discuss/269517/Python-Graph-BFS
        :type A: str
        :type B: str
        :rtype: int
        """
        # level = 0
        # q = [A]
        # visit = set()
        # while q:
        #     l = len(q)
        #     for i in range(l):
        #         curr = q.pop(0)
        #         if curr == B:
        #             return level
        #         for i in range(len(A)-1):
        #             for j in range(i+1, len(A)):
        #                 s = list(curr[:])
        #                 s[i],s[j] = s[j],s[i]
        #                 s = ''.join(s)
        #                 if s not in visit:
        #                     visit.add(s)
        #                     q.append(s)
        #     level += 1
        # return level
        def getNeighbor(x):
            i = 0
            while x[i] == B[i]:
                i += 1
            lst = []
            for j in range(i+1, len(x)):
                if x[j] == B[i]:
                    lst.append(x[:i]+x[j]+x[i+1:j]+x[i]+x[j+1:])
            return lst

        level = 0
        q = [A]
        visit = set([A])
        while q:
            l = len(q)
            for _ in range(l):
                curr = q.pop(0)
                if curr == B:
                    return level
                for nei in getNeighbor(curr):
                    if nei not in visit:
                        visit.add(nei)
                        q.append(nei)
            level += 1
        return level

print Solution().kSimilarity('ab','ba')
print Solution().kSimilarity('abc','bca')
print Solution().kSimilarity('abac','baca')
print Solution().kSimilarity('abacdefbacaefd','bacaefdabacdef')
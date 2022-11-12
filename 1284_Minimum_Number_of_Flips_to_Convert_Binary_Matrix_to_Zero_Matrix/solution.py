class Solution(object):
    def minFlips(self, mat):
        """
        BFS
        T:O(2^mn) S:O(2^mn)
        Runtime: 44 ms, faster than 58.51% of Python online submissions for Minimum Number of Flips to Convert Binary Matrix to Zero Matrix.
        Memory Usage: 12.9 MB, less than 36.84% of Python online submissions for Minimum Number of Flips to Convert Binary Matrix to Zero Matrix.
        :type mat: List[List[int]]
        :rtype: int
        """
        m, n = len(mat), len(mat[0])

        def flip(s, i):
            ans = s[:]
            ans[i] = 0 if ans[i] == 1 else 1
            if i - n >= 0:
                ans[i-n] = 0 if ans[i-n] == 1 else 1
            if i + n < m*n:
                ans[i+n] = 0 if ans[i+n] == 1 else 1
            if i % n != 0:
                ans[i-1] = 0 if ans[i-1] == 1 else 1
            if i % n != n-1:
                ans[i+1] = 0 if ans[i+1] == 1 else 1
            return ans

        start = []
        for i in range(m):
            for j in range(n):
                start.append(mat[i][j])
        q = [start]
        visit = set([''.join([str(x) for x in start])])
        count = 0
        while q:
            l = len(q)
            for _ in range(l):
                s = q.pop(0)
                if sum(s) == 0:
                    return count
                for i in range(len(s)):
                    nxt_state = flip(s, i)
                    key = ''.join(''.join([str(x) for x in nxt_state]))
                    if key not in visit:
                        visit.add(key)
                        q.append(nxt_state)
            count += 1
        return -1

print Solution().minFlips([[1,1,1],[1,0,1],[0,0,0]])
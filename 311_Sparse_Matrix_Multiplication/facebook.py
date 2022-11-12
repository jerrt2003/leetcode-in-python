class Solution(object):
    def multiply(self, A, B):
        """
        Facebook
        https://leetcode.com/problems/sparse-matrix-multiplication/discuss/419538/What-the-interviewer-is-expecting-when-this-problem-is-asked-in-an-interview...
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """

        def findNoneZero(matrix):
            ret = []
            m, n = len(matrix), len(matrix[0])
            for i in range(m):
                for j in range(n):
                    if matrix[i][j] != 0:
                        ret.append([i, j])
            return ret

        nonA = findNoneZero(A)
        nonB = findNoneZero(B)

        m, n = len(A), len(A[0])
        p, q = len(B), len(B[0])

        ans = [[0 for _ in range(q)] for _ in range(m)]

        for a_row, a_col in nonA:
            for b_row, b_col in nonB:
                if a_col == b_row:
                    ans[a_row][b_col] += A[a_row][a_col] * B[b_row][b_col]

        return ans

print Solution().multiply([[1,0,0],[-1,0,3]],[[7,0,0],[0,0,0],[0,0,1]])
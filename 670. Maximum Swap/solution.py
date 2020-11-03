class Solution(object):
    def maximumSwap(self, num):
        """
        Facebook
        T:O(n * 9) S:O(n)
        Runtime: 20 ms, faster than 62.61% of Python online submissions for Maximum Swap.
        Memory Usage: 12.6 MB, less than 80.65% of Python online submissions for Maximum Swap.
        :type num: int
        :rtype: int
        """
        A = map(int, str(num))
        last_idx = [-1] * 10
        for i, v in enumerate(A):
            last_idx[v] = i
        for i, v in enumerate(A):
            for j in range(9, v, -1):
                if last_idx[j] != -1 and last_idx[j] > i:
                    A[i], A[last_idx[j]] = A[last_idx[j]], A[i]
                    return int(''.join(str(d) for d in A))
        return num

print Solution().maximumSwap(9934)
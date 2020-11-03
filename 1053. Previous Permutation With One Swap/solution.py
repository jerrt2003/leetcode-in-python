class Solution(object):
    def prevPermOpt1(self, A):
        """
        :type A: List[int]
        :rtype: List[int]
        """
        i = len(A)-1
        while i > 0:
            if A[i-1] > A[i]:
                break
            i -= 1
        if i == 0:
            return A
        idx = i
        j = len(A)-1
        while j > i-1:
            if A[j] < A[i-1] and A[j] > A[idx]:
                idx = j
            j -= 1
        A[idx], A[i-1] = A[i-1], A[idx]
        return A


print Solution().prevPermOpt1([1,9,4,6,7])
print Solution().prevPermOpt1([3,1,1,3])
print Solution().prevPermOpt1([3,2,1])
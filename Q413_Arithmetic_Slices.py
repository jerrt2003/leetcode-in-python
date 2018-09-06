class Solution(object):
    '''
    def numberOfArithmeticSlices(self, A):
        """
        Brutal Force
        :type A: List[int]
        :rtype: int
        """
        count = 0
        for i in range(len(A)-1):
            dist = A[i+1] - A[i]
            for j in range(i+1, len(A)-1):
                if A[j+1] - A[j] == dist:
                    count += 1
                else:
                    break
        return count
    '''

    '''
    def numberOfArithmeticSlices(self, A):
        """
        Recursive (TOP-BOTTOM)
        :type A: List[int]
        :rtype: int
        """
        self.sum = 0
        self._slice(A, len(A)-1)
        return self.sum

    def _slice(self, A, i):
        ap = 0
        if i < 2:
            return 0
        elif A[i] - A[i-1] == A[i-1] - A[i-2]:
            ap = 1 + self._slice(A, i-1)
            self.sum += ap
        else:
            self._slice(A, i-1)
        return ap
    '''

    def numberOfArithmeticSlices(self, A):
        """
        DP Solution (Bottom-Up)
        :type A: List[int]
        :rtype: int
        """
        total_sum = 0
        DP = dict()
        DP[0] = 0
        DP[1] = 0
        for i in range(2, len(A)):
            if A[i] - A[i-1] == A[i-1] - A[i-2]:
                DP[i] = 1 + DP[i-1]
                total_sum += DP[i]
            else:
                DP[i] = 0
        return total_sum


#A = [1, 2, 3, 4]
A= [1, 3, 5, 7, 9]
#A = [1,2,3,8,9,10]
sol = Solution()
print sol.numberOfArithmeticSlices(A)
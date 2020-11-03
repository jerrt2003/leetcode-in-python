import collections

class Solution(object):
    def minDominoRotations(self, A, B):
        """
        T:O(nlogn) S:O(n)
        Runtime: 1264 ms, faster than 29.92% of Python online submissions for Minimum Domino Rotations For Equal Row.
        Memory Usage: 14 MB, less than 100.00% of Python online submissions for Minimum Domino Rotations For Equal Row.
        :type A: List[int]
        :type B: List[int]
        :rtype: int
        """
        counter_A = collections.Counter(A)
        counter_B = collections.Counter(B)
        rank = []
        for k, v in counter_A.iteritems():
            rank.append(['A', k, v])
        for k, v in counter_B.iteritems():
            rank.append(['B', k, v])
        rank.sort(key=lambda x: (-x[2], x[1], x[0]))
        for half, k, _ in rank:
            if half == 'A':
                count = 0
                finish = True
                for i in range(len(A)):
                    if A[i] != k and B[i] != k:
                        finish = False
                        break
                    elif A[i] != k and B[i] == k:
                        count += 1
                if finish:
                    return count
            elif half == 'B':
                count = 0
                finish = True
                for i in range(len(A)):
                    if B[i] != k and A[i] != k:
                        finish = False
                        break
                    elif B[i] != k and A[i] == k:
                        count += 1
                if finish:
                    return count
        return -1

print Solution().minDominoRotations([2,1,2,4,2,2],[5,2,6,2,3,2])
print Solution().minDominoRotations([3,5,1,2,3], [3,6,3,3,4])
print Solution().minDominoRotations([0,0,0,0,0],[1,2,3,4,5])
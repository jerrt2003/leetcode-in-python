class Solution(object):
    def intervalIntersection(self, A, B):
        """
        :type A: List[List[int]]
        :type B: List[List[int]]
        :rtype: List[List[int]]
        """
        i = j = 0
        res = []
        while i < len(A) and j < len(B):
            s = max(A[i][0], B[j][0])
            e = min(B[i][1], B[j][1])
            res.append([s,e])
            if A[i][1] < B[j][1]:
                i += 1
            else:
                j += 1
        return res


# print Solution().intervalIntersection([[0,2],[5,10],[13,23],[24,25]],[[1,5],[8,12],[15,24],[25,26]])
print Solution().intervalIntersection([[3,5],[9,20]],[[4,5],[7,10],[11,12],[14,15],[16,20]])
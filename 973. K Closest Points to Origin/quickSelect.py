class Solution(object):
    def kClosest(self, points, K):
        """
        Facebook
        T:O(n) S:O(1)
        Runtime: 656 ms, faster than 62.49% of Python online submissions for K Closest Points to Origin.
        Memory Usage: 18.3 MB, less than 96.55% of Python online submissions for K Closest Points to Origin.
        :type points: List[List[int]]
        :type K: int
        :rtype: List[List[int]]
        """

        def distance(x):
            return points[x][0] * points[x][0] + points[x][1] * points[x][1]

        def partition(l, r):
            pivot = distance(r)
            i = l
            for j in range(l, r):
                if distance(j) < pivot:
                    points[i], points[j] = points[j], points[i]
                    i += 1
            points[i], points[r] = points[r], points[i]
            return i

        def quickSelect(l, r, k):
            if l < r:
                pt = partition(l, r)
                if pt == k:
                    return pt
                elif pt > k:
                    return quickSelect(l, pt - 1, k)
                else:
                    return quickSelect(pt + 1, r, k)

        quickSelect(0, len(points) - 1, K)
        return points[:K]


print Solution().kClosest([[0,1],[1,0]],2)
print Solution().kClosest([[1,3],[-2,2]],1)
print Solution().kClosest([[1,3],[-2,2]],1)
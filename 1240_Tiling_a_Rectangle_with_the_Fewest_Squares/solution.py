class Solution(object):
    def tilingRectangle(self, n, m):
        """
        :type n: int
        :type m: int
        :rtype: int
        """
        def dfs(k, area, count):
            if area == 0:
                return count
            for i in range(k, 0, -1):
                if area - i*i >= 0:
                    ret = dfs(i, area-i*i, count+1)
                    if ret != -1:
                        return ret
            return -1

        limit = min(n,m)
        return dfs(limit, n*m, 0)

# print Solution().tilingRectangle(2, 3)
# print Solution().tilingRectangle(5, 8)
print Solution().tilingRectangle(11, 13)
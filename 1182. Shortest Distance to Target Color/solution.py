import collections

class Solution(object):
    def shortestDistanceColor(self, colors, queries):
        """
        S:O(n + mlog(n)) S:O(n)
        Runtime: 1936 ms, faster than 45.16% of Python online submissions for Shortest Distance to Target Color.
        Memory Usage: 37.3 MB, less than 100.00% of Python online submissions for Shortest Distance to Target Color.
        :type colors: List[int]
        :type queries: List[List[int]]
        :rtype: List[int]
        """
        color2idx = collections.defaultdict(list)
        for i, c in enumerate(colors):
            color2idx[c].append(i)

        ans = []
        for query in queries:
            idx, color = query[0], query[1]
            if color not in color2idx.keys():
                ans.append(-1)
                continue
            arr = color2idx[color]
            l, r = 0, len(arr)
            while l < r:
                m = (l+r-1)//2
                if arr[m] >= idx:
                    r = m
                else:
                    l = m+1
            if l == len(arr):
                ans.append(idx-arr[-1])
            elif arr[l] == idx:
                ans.append(0)                
            elif l == 0:
                ans.append(arr[0]-idx)
            else:
                ans.append(min(idx-arr[l-1], arr[l]-idx))
        return ans

# print(Solution().shortestDistanceColor([1,1,2,1,3,2,2,3,3],[[1,3],[2,2],[6,1]]))
# print(Solution().shortestDistanceColor([1,2],[[0,3]]))
print(Solution().shortestDistanceColor([3,1,1,2,3,3,2,1,2,3,1,1,3,2,3,1,1,1,1,2,2,1,2,2,2,1,1,1,1,2,3,3,3,1,3,2,1,1,2,2,1,3,1,2,1,1,2,2,1,2],[[10,2],[0,1],[32,3],[1,1],[41,1],[48,3],[0,3],[46,2],[48,2],[28,1],[47,2],[11,2],[49,3],[3,3],[40,1],[1,2],[42,2],[47,2],[36,3],[23,1],[7,3],[47,2],[13,3],[36,1],[17,2],[46,2],[38,2],[0,1],[38,3],[36,3],[33,1],[11,3],[39,2],[10,2],[44,3],[5,1],[36,3],[44,3],[38,1],[9,1],[9,1],[35,3],[10,1],[9,1],[0,3],[1,1],[0,3],[28,1],[22,3],[15,1]]))
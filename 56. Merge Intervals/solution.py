class Solution(object):
    def merge(self, intervals):
        """
        Facebook
        T:O(nlogn) S:O(n)
        Runtime: 16 ms, faster than 31.75% of Go online submissions for Merge Intervals.
        Memory Usage: 4.7 MB, less than 45.62% of Go online submissions for Merge Intervals.
        :type intervals: List[List[int]]
        :rtype: List[List[int]]
        """
        intervals.sort(key=lambda x: x[0])
        ans = []
        for s, e in intervals:
            if not ans or s > ans[-1][1]:
                ans.append([s, e])
                continue
            if e < ans[-1][1]:
                continue
            if s <= ans[-1][1] <= e:
                pre = ans.pop()
                pre_s, pre_e = pre[0], pre[1]
                ans.append([pre_s, e])
        return ans


print Solution().merge([[1,4],[2,3]])
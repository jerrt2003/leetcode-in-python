import collections


class Solution(object):
    def largestValsFromLabels(self, values, labels, num_wanted, use_limit):
        """
        T:O(nlogn) S:O(n)
        Runtime: 148 ms, faster than 42.57% of Python online submissions for Largest Values From Labels.
        Memory Usage: 19.6 MB, less than 100.00% of Python online submissions for Largest Values From Labels.
        :type values: List[int]
        :type labels: List[int]
        :type num_wanted: int
        :type use_limit: int
        :rtype: int
        """
        lst = [_ for _ in zip(values, labels)]
        lst.sort(key=lambda x: (-x[0],x[1]))
        ans = 0
        bkt = collections.defaultdict(int)
        for value, label in lst:
            if bkt[label] < use_limit:
                ans += value
                bkt[label] += 1
                num_wanted -= 1
            if num_wanted == 0:
                break
        return ans


# print Solution().largestValsFromLabels([5,4,3,2,1],[1,3,3,3,2],3,2)
print Solution().largestValsFromLabels([9,8,8,7,6],[0,0,0,1,1],3,2)
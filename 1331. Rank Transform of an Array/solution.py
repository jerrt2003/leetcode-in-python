class Solution(object):
    def arrayRankTransform(self, arr):
        """
        T:O(n) S:(n)
        Runtime: 332 ms, faster than 82.28% of Python online submissions for Rank Transform of an Array.
        Memory Usage: 31.8 MB, less than 100.00% of Python online submissions for Rank Transform of an Array.
        :type arr: List[int]
        :rtype: List[int]
        """
        num_set = list(set(arr))
        rank = dict()
        for i, v in enumerate(sorted(num_set)):
            rank[v] = i+1

        for i in range(len(arr)):
            arr[i] = rank[arr[i]]

        return arr
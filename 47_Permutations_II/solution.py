import collections


class Solution(object):
    def permuteUnique(self, nums):
        """
        Facebook
        T:O(n) S:O(n)
        Runtime: 44 ms, faster than 81.41% of Python online submissions for Permutations II.
        Memory Usage: 12.9 MB, less than 56.41% of Python online submissions for Permutations II.
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        counter = collections.Counter(nums)
        ans = []

        def helper(path):
            if len(path) == len(nums):
                ans.append(path)
                return
            for k, v in counter.iteritems():
                if v > 0:
                    counter[k] -= 1
                    helper(path + [k])
                    counter[k] += 1

        helper([])
        return ans

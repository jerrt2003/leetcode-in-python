import collections


class Solution(object):
    def topKFrequent(self, nums, k):
        """
        Facebook
        Quick Select
        T:O(n) S:O(n)
        Runtime: 88 ms, faster than 90.57% of Python online submissions for Top K Frequent Elements.
        Memory Usage: 16.1 MB, less than 87.65% of Python online submissions for Top K Frequent Elements.
        :type nums: List[int]
        :type k: int
        :rtype: List[int]
        """
        counter = collections.Counter(nums)
        self.lst = counter.keys()

        def partition(l, r):
            pivot = counter[self.lst[r]]
            i = l
            for j in range(l, r):
                if counter[self.lst[j]] > pivot:
                    self.lst[i], self.lst[j] = self.lst[j], self.lst[i]
                    i += 1
            self.lst[i], self.lst[r] = self.lst[r], self.lst[i]
            return i

        def quickSelect(l, r, k):
            if l == r:
                return
            pt = partition(l, r)
            if pt == k:
                return pt
            elif pt < k:
                return quickSelect(pt+1, r, k)
            else:
                return quickSelect(l, pt-1, k)

        quickSelect(0, len(self.lst)-1, k)
        return self.lst[:k]


# print Solution().topKFrequent([8,8,8,8,9,9,9,10,10,11], 2)
print Solution().topKFrequent([1],1)
import collections


class Solution(object):
    def numSmallerByFrequency(self, queries, words):
        """
        T:O(nlogn) S:O(n)
        Runtime: 132 ms, faster than 63.33% of Python online submissions for Compare Strings by Frequency of the Smallest Character.
        Memory Usage: 13.4 MB, less than 75.00% of Python online submissions for Compare Strings by Frequency of the Smallest Character.
        :type queries: List[str]
        :type words: List[str]
        :rtype: List[int]
        """
        def freq(w):
            counter = collections.Counter(w)
            key = sorted(counter.keys())
            return counter[key[0]]

        w_freq = [freq(w) for w in words]
        w_freq.sort()

        ans = []
        for q in queries:
            freq_q = freq(q)
            l, r = 0, len(w_freq)
            while l < r:
                mid = (l+r-1)/2
                if w_freq[mid] > freq_q:
                    r = mid
                else:
                    l = mid+1
            ans.append(len(w_freq)-l)
        return ans
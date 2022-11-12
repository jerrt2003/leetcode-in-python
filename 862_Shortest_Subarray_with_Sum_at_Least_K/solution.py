import collections


class Solution(object):
    def shortestSubarray(self, A, K):
        """
        sliding window + monotonic queue
        T:O(n) S:O(n)
        Runtime: 740 ms, faster than 96.44% of Python online submissions for Shortest Subarray with Sum at Least K.
        Memory Usage: 18.5 MB, less than 75.44% of Python online submissions for Shortest Subarray with Sum at Least K.
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        prefix = [0]
        for x in A:
            prefix.append(x+prefix[-1])

        ans = float('inf')
        monoq = collections.deque()
        for y, Py in enumerate(prefix):
            while monoq and Py - prefix[monoq[0]] >= K:
                ans = min(ans, y-monoq.popleft())
            while monoq and Py <= prefix[monoq[-1]]:
                monoq.pop()
            monoq.append(y)
        return ans if ans != float('inf') else -1

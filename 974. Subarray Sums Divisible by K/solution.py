class Solution(object):
    def subarraysDivByK(self, A, K):
        """
        Facebook
        prefix sum
        hash table
        A: current prefix sum
        B: any of the previous prefix sum
        A - B: sum between current num to any of the previous num
        A - B = n * k --> A % k - B % k = (n*k) % k --> A % k = B % k

        curr prefix sum mod = (B + a) % k --> B: any previous prefix, a: curr num
                            = (n*k + b + a) % k --> b: previous B mod
                            = b % k + a % k
                            = (a + b) % k
        T:O(n) S:O(n)
        Runtime: 320 ms, faster than 44.30% of Python online submissions for Subarray Sums Divisible by K.
        Memory Usage: 16 MB, less than 71.08% of Python online submissions for Subarray Sums Divisible by K.
        :type A: List[int]
        :type K: int
        :rtype: int
        """
        res = 0
        prefix = [1] + [0] * (K-1)
        pre_sum = 0
        for a in A:
            pre_sum = (pre_sum + a) % K
            res += prefix[pre_sum]
            prefix[pre_sum] += 1
        return res
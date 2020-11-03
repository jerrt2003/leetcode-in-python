class Solution(object):
    def sumSubarrayMins(self, A):
        """
        Stack Mono-Q
        T:O(n) S:O(n)
        Runtime: 540 ms, faster than 43.64% of Python online submissions for Sum of Subarray Minimums.
        Memory Usage: 17.6 MB, less than 35.06% of Python online submissions for Sum of Subarray Minimums.
        https://leetcode.com/problems/sum-of-subarray-minimums/discuss/178876/stack-solution-with-very-detailed-explanation-step-by-step
        https://leetcode.com/problems/sum-of-subarray-minimums/discuss/170750/C%2B%2BJavaPython-Stack-Solution
        :type A: List[int]
        :rtype: int
        """
        mod = 10**9 + 7
        L, R, stack = [],[],[]
        for a in A:
            count = 1
            while stack and a < stack[-1][0]: #!!
                _, c = stack.pop()
                count += c
            stack.append((a, count))
            L.append(count)
        stack = []
        for a in A[::-1]:
            count = 1
            while stack and a <= stack[-1][0]: #!! handle duplicates
                _, c = stack.pop()
                count += c
            stack.append((a, count))
            R.append(count)
        R = R[::-1]
        ans = 0
        for i in range(len(A)):
            ans += L[i]*R[i]*A[i]
        return ans % mod


print Solution().sumSubarrayMins([3,1,2,4])
print Solution().sumSubarrayMins([3,1,2,1,4])
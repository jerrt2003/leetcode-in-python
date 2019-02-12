'''
import math
class Solution(object):
    def numSquares(self, n):
        """
        DP Solution 1st version: TLE
        :type n: int
        :rtype: int
        """
        def n_logarithmic_check(n): #check if given number has square root
            i = math.sqrt(n)
            if (i - int(i))*10 != 0:
                return False
            else:
                return True

        if n_logarithmic_check(n):
            return 1
        else:
            DP = [1,1,2]
            for i in range(3, n+1):
                if n_logarithmic_check(i):
                    DP.append(1)
                else:
                    count = i
                    for j in range(1,i):
                        # Try to divide the number into combination of
                        count = min(count, DP[j]+DP[i-j])
                    DP.append(count)
        return DP[n]
'''


class Solution(object):
    def numSquares(self, n):
        """
        Solution: DP
        Time Complexity: O(n^2)
        Space Complexity: O(n)
        Inspired By: 1st scan
        Perf: Runtime: 2892 ms, faster than 55.18% / Memory Usage: 10.8 MB, less than 15.94%
        :type n: int
        :rtype: int
        """
        if n <= 0:
            return 0
        DP = [0,1]
        for i in range(2,n+1):
            count = n
            j = 1
            while j*j <= i:
                #DP[i-j*j] stands for min squares for DP[i-j*j]
                #+1 stands for the j*j combination
                #因為使用j*j所以逼近較快
                count = min(count, DP[i-j*j]+1)
                j += 1
            DP.append(count)
        return DP[n]





n = 16
sol = Solution()
print sol.numSquares(n)
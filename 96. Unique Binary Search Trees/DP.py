# -*- coding: utf-8 -*-
class Solution(object):
    def numTrees(self, n):
        """
        Solution: DP
        Time Complexity: O(n^2)
        Space Complexity: O(n)
        Inspired By: https://leetcode.com/problems/unique-binary-search-trees/discuss/31707/Fantastic-Clean-Java-DP-Solution-with-Detail-Explaination
        Thinking Process:
        - Let's said we already know ways to build tree from 1~4 which is DP[0]=1, DP[1]=1, DP[2]=2, DP[3]=5, DP[4]=14
        - To build a tree {1,2,3,4,5}
        - First pick "1" as root:
            - {2,3,4,5} must be in the right side
            - So total combination will be DP[0]*DP[4] = 14 (DP[0] stands for no side on the left and DP[4] stands for 4 nodes on the right)
        - Then we pick "2" as root:
            - {3,4,5} must be in the right side
            - So total combination will be DP[1]*DP[3] = 10 (DP[1] stands for one node on the left and DP[3] 3 nodes on the right)
        - Total sum will be all DP[i] sum up
        - 像個鎖鏈一路拉過去...
        Algorithm:
        - DP = [1,1,2]
        - For i in range(2, n+1):
            tmp = 0
            For root in range(1,i+1):
                tmp += DP[root-1]*DP[i-root]
            DP[i] = tmp
          return DP[-1]
        :type n: int
        :rtype: int
        """
        DP = [1,1]
        for i in range(2, n+1):
            tmp = 0
            for root in range(1, i+1):
                tmp += DP[root-1]*DP[i-root]
            DP.append(tmp)
        return DP[-1]

n = 4
sol = Solution()
print sol.numTrees(n)

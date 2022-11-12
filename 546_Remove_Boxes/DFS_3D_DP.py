# -*- coding: utf-8 -*-
class Solution(object):
    def removeBoxes(self, boxes):
        """
        Solution: DFS + 3D DP
        Time Complexity: O(n^4)
        Space Complexity: O(n^3)
        Inspired By: https://www.youtube.com/watch?v=wT7aS5fHZhs
        TP:
        - my original method didn't take "removing" order into consideration.
            - for example [5,3,5,1,5], by removing 3, 1 first will yield maximum result
        - So how we going to resolve this problem?
        - We'll introduce 3 variables:
            - l: left idx
            - r: right idx
            - k: number of boxes which has same color as boxes[r] following boxes[r] (more on this later)
        - Still use [5,3,5,1,5] as example:
            - we have 2 types of way of removing boxes,
                - one by one (from either start or end) (base case)
                    - ex. [5,3,5,1] [5] (remove last 5)
                - or we remove some boxes in the middle and try to put same color boxes together so we can have maximum output (special case)
                    - ex. [5,3,5,5] [1] (remove 1 first)
                    - so now we have one 5 following [5,3,5] sub-array to form [5,3,5,5], and this number is our "k" (now this k is 1)
        - So now let's move to our dfs function:
            - if l > r: means no more boxes left, return 0
            - if (l, r, k) is found in DP, then we don't need to calculate it again, just return DP[(l, r, k)]
            - base case: self.DP[(l,r,k)] = self.dfs(boxes, l, r-1, 0) + (k+1)*(k+1)
            - specail case: self.DP[(l, r, k)] = max(self.DP[(l,r,k)], self.dfs(boxes,i+1,r-1,0) + self.dfs(boxes,l,i,k+1)
        :type boxes: List[int]
        :rtype: int
        """
        self.DP = dict()
        return self.dfs(boxes, 0, len(boxes)-1, 0)


    def dfs(self, boxes, l, r, k):
        if l > r:
            return 0
        if (l, r, k) in self.DP: return self.DP[(l, r, k)]
        # we can optimize code for situation like [1,1,1,1,1,1,1,1....1,1,1,1]
        while l < r:
            if boxes[r] == boxes[r-1]:
                k += 1
                r -= 1
            else:
                break
        # base cases
        self.DP[(l, r, k)] = self.dfs(boxes, l, r-1, 0) + (k+1)*(k+1)
        # 2nd case
        for i in range(l, r):
            if boxes[i] == boxes[r]:
                self.DP[(l, r, k)] = max(self.DP[(l, r, k)], self.dfs(boxes, i+1, r-1, 0) + self.dfs(boxes, l, i, k+1))
        return self.DP[(l, r, k)]

boxes = [1, 3, 2, 2, 2, 3, 4, 3, 1]
sol = Solution()
print sol.removeBoxes(boxes)
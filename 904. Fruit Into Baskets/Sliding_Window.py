# -*- coding: utf-8 -*-
class Solution(object):
    def totalFruit(self, tree):
        """
        Solution: sliding window
        Time Complexity: O(n)
        Space Complexity: O(n)
        Inspired By:
        - https://leetcode.com/problems/fruit-into-baskets/solution/
        - https://leetcode.com/problems/fruit-into-baskets/discuss/170740/Sliding-Window
        TP:
        - Translate: What is the longest sub-array which contain at most 2 elements?
            - ex. [1,2,3,3,4,5] -> ans: [2,3,3] is longest sub-array contain at most 2 elements
        :type tree: List[int]
        :rtype: int
        """
        i = res = 0
        basket = {} # create our basket (dict)
        for j, v in enumerate(tree): # !! using enumerate to get indices for each tree
            basket[v] = basket.get(v, 0)+1 # go through the tree from left to right and add 'fruit' into basket
            # if basket contain more than 2 'fruits', we need to start move the index i to right to maintain condition
            # that basket can have at most 2 'fruits' int the basket
            while len(basket) > 2:
                basket[tree[i]] -= 1
                if basket[tree[i]] == 0:
                    del basket[tree[i]]
                i += 1
            res = max(res, j-i+1)
            '''
            ex. [1,1,2,2,3,4]
            when j move to 4, basket will be: {1:2, 2:2, 3:1}, so we hit while condition, then we start to move index i (at this moment i=0)
            after first while loop, basket become {1:1, 2:2, 3:1}, now we still have 3 'fruits' in the basket, so we need to move i again (i=1),
            after 2nd while loop, basket become {2:2, 3:1} which len(basket) == 2, so we exist while loop and calculate the sub-array length
            4 - 2 +1 (j-i+1) = 3
            '''

        return res

#tree = [1,2,1]
#tree = [0,1,2,2]
#tree = [1,2,3,2,2]
#tree = [3,3,3,1,2,1,1,2,3,3,4]
tree = []

print Solution().totalFruit(tree)
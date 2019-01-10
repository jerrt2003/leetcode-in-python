# -*- coding: utf-8 -*-
class Solution(object):
    def spiralOrder(self, matrix):
        """
        Solution: Go through matrix
        Time Complexity: O(mn)
        Space Complexity: O(mn)
        Inspired By:
        - MYSELF
        - https://leetcode.com/problems/spiral-matrix/discuss/20656/AC-Python-32ms-solution
        TP:
        - 建立起點跟終點
        - 利用for loop的start, end, step 按著順序走
        :type matrix: List[List[int]]
        :rtype: List[int]
        """
        if not matrix or not matrix[0]: return []
        res = []
        i_start = 0
        i_end = len(matrix) - 1
        '''
        WHY i_end is len(matrix)-1 ?
        為了避免idx out of range. 我們會在下一個行(列)iteration時把最後一個數給補上!!
        '''
        j_start = 0
        j_end = len(matrix[0]) - 1
        while i_start < i_end and j_start < j_end:
            res.extend(matrix[i_start][x] for x in range(j_start, j_end))
            res.extend(matrix[x][j_end] for x in range(i_start, i_end))
            res.extend(matrix[i_end][x] for x in range(j_end, j_start, -1))
            res.extend(matrix[x][j_start] for x in range(i_end, i_start, -1))
            i_start += 1
            i_end -= 1
            j_start += 1
            j_end -= 1
        '''
        為什麼最後一定是由左向右(或者是上到下)的順序？
        因為在上方iteration時我們一定是作完了left_to_right->up_to_down->right_to_left->down_to_up整套,所以剩下的一定是left_to_right or up_to_down
        '''
        if i_start == i_end:
            res.extend(matrix[i_start][x] for x in range(j_start, j_end+1)) # WHY i_end+1 or j_end+1 <-- 沒有下一個iteration了,所以必須要包含最後一個數字
        elif j_start == j_end:
            res.extend(matrix[x][j_start] for x in range(i_start, i_end+1))
        return res



'''
matrix = [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]
'''
matrix = [[1,2,3,4,5,6,7,8,9,10]]

sol = Solution()
print sol.spiralOrder(matrix)
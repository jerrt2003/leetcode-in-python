from typing import List

class Solution:
    def minArea(self, image: List[List[str]], x: int, y: int) -> int:
        if len(image) == 0:
            return 0
        m, n = len(image), len(image[0])
        # 我們首先做個'壓縮'(i.e.把image含有'1'的row/col範圍找出來)
        # 相當於把2D的資訊壓成兩個1D的數列組
        row = [0] * m
        col = [0] * n
        for i in range(m):
            for j in range(n):
                if image[i][j] == "1":
                    row[i] = 1
                    col[j] = 1
        # 根據row數列組找出1的上下邊界
        # ex. [0,1,1,1,0,0] -> lower: 1, upper: 3
        # find lower bound for x
        l, r = 0, x+1
        while l < r:
            mid = (l+r-1)//2
            if row[mid] == 1:
                r = mid
            else:
                l = mid+1
        lower_row_bound = l
        # find upper bound for x
        l, r = x, m
        while l < r:
            mid = (l+r-1)//2
            if row[mid] == 0:
                r = mid
            else:
                l = mid+1
        upper_row_bound= l-1
        min_row_length = upper_row_bound - lower_row_bound + 1
        # 根據col數列組找出1的上下邊界
        # ex. [0,1,1,1,0,0] -> lower: 1, upper: 3
        # find lower bound for y
        l, r = 0, y+1
        while l < r:
            mid = (l+r-1)//2
            if col[mid] == 1:
                r = mid
            else:
                l = mid+1
        lower_col_bound = l
        # find upper bound for y
        l, r = y, n
        while l < r:
            mid = (l+r-1)//2
            if col[mid] == 0:
                r = mid
            else:
                l = mid+1
        upper_col_bound= l-1
        min_col_length = upper_col_bound - lower_col_bound + 1

        return min_row_length*min_col_length
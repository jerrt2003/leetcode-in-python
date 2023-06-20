from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        # 當數組為空時，直接返回空數組
        if not matrix:
            return []
        ans = []
        # 首先设定上下左右边界
        l, r, u, b = 0, len(matrix[0])-1, 0, len(matrix)-1
        while True:
            # 其次向右移动到最右，此时第一行因为已经使用过了，可以将其从图中删去，体现在代码中就是重新定义上边界
            for j in range(l, r+1):
                ans.append(matrix[u][j])
            # 重新定義上邊界 
            u += 1
            # 判断若重新定义后，上下边界交错，表明螺旋矩阵遍历结束，跳出循环，返回答案
            if u > b: break
            for i in range(u, b+1):
                ans.append(matrix[i][r])
            r -= 1
            if l > r: break
            for j in range(r, l-1, -1):
                ans.append(matrix[b][j])
            b -= 1
            if u > b: break
            for i in range(b, u-1, -1):
                ans.append(matrix[i][l])
            l += 1
            if l > r: break
        return ans

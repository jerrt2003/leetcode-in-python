import collections
from typing import List


class Solution:
    def findRLEArray(
        self, encoded1: List[List[int]], encoded2: List[List[int]]
    ) -> List[List[int]]:
        # 代码首先定义了两个指针i和j，分别用于遍历两个输入的编码数组。
        # 然后定义了一个空的答案数组ans，用于存储最终的结果。
        i, j = 0, 0
        ans = []
        # 使用一个while循环，当两个指针都没有走到各自数组的尾部时，执行以下操作
        while i < len(encoded1) and j < len(encoded2):
            # 计算两个当前指向的元素的频率的最小值count，这是因为乘积的频率应该为两个元素频率的最小值。
            count = min(encoded1[i][1], encoded2[j][1])
            # 如果ans为空，或者ans的最后一个元素的值不等于两个当前元素的乘积，
            # 那么就在ans后面添加一个新的元素，其值为两个当前元素的乘积，频率为count。
            if not ans or ans[-1][0] != encoded1[i][0] * encoded2[j][0]:
                ans.append([encoded1[i][0] * encoded2[j][0], count])
            # 否则，就将ans的最后一个元素的频率加上count。(壓縮)
            else:
                ans[-1][1] += count
            # 最后，更新两个当前元素的频率，减去count。如果某个元素的频率变为0，那么就向前移动相应的指针。
            encoded1[i][1] -= count
            encoded2[j][1] -= count
            if encoded1[i][1] == 0:
                i += 1
            if encoded2[j][1] == 0:
                j += 1

        return ans

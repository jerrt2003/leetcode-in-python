from typing import List

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        # 用二分法找出idx, arr[idx]為大於等於x的最小值
        l, r = 0, len(arr)
        while l < r:
            m = (l+r-1)//2
            # 為什麼是arr[m] >= x 萬一 x=3, arr=[1,2,9,7] k=1 怎麼辦？這樣不是會找到9嗎？
            # 不用擔心 在等等左右邊界收縮時就會解決這個問題
            if arr[m] >= x:
                r = m
            else:
                l = m+1
        # 以idx為中心左右擴展k個數 
        # 注意左右boundry為0以及len(arr)-1 
        # 然後從左右邊界開始收縮直到rb-lb+1==k為止
        lb, rb = max(0, l-k), min(len(arr)-1, l+k)
        while rb-lb+1 > k:
            if arr[rb]-x >= x-arr[lb]:
                rb -= 1
            else:
                lb += 1
        return arr[lb:rb+1]
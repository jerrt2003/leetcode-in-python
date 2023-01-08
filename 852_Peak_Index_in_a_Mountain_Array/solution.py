from typing import List

class Solution:
    def peakIndexInMountainArray(self, arr: List[int]) -> int:
        l, r = 0, len(arr)
        while l < r:
            m = (l+r-1)//2
            # 找出一個最小 m 而arr[m] > arr[m+1]（峰值)
            # 為什麼用arr[m] > arr[m+1]而不選擇arr[m-1]<arr[m]呢？處理邊界問題
            # 當使用arr[m-1]而 m剛好為0時arr[m-1]=arr[-1]Python會用arr最後一個元素
            if arr[m] > arr[m+1]:
                r = m
            else:
                l = m+1
        return l
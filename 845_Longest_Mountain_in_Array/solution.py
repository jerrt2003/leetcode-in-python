from typing import List

class Solution:
    def longestMountain(self, arr: List[int]) -> int:
        n = len(arr)
        # left_arr: 以i為山頂 往左最多可以延伸的距離 
        # 從山頂往左應該嚴格維持arr[i-1]<arr[i]的條件
        left_arr = [0] * n
        # right_arr: 以i為山頂 往右最多可以延伸的距離 
        # 從山頂往左應該嚴格維持arr[i]>arr[i+1]的條件        
        right_arr = [0] * n
        # 由左往右 idx從1開始 因為idx=0時往左無法延伸所以一定為0
        # left_arr[0] = 0 相當於DP的初始條件
        for i in range(1, n):
            if arr[i-1] < arr[i]:
                left_arr[i] = left_arr[i-1] + 1
        # 由右往左 idx從n-2開始 因為idx=n-1時往右無法延伸所以一定為0
        # right_arr[n-1] = 0 相當於DP的初始條件                
        for i in range(n-2, -1, -1):
            if arr[i] > arr[i+1]:
                right_arr[i] = right_arr[i+1] + 1
        ans = 0
        # 枚舉(遍歷)i 當left_arr[i]>0且right_arr[i]>0 
        # 此時i為山頂：因為往左往右皆可以延伸
        for i in range(n):
            if left_arr[i] > 0 and right_arr[i] > 0:
                # 記得加上自己 1+left_arr[i]+right_arr[i]
                ans = max(ans, 1 + left_arr[i] + right_arr[i])
        
        return ans
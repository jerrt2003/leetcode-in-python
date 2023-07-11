class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        prefix = []
        for i, v in enumerate(arr):
            if not prefix:
                prefix.append(v - 1)
            else:
                prefix.append(prefix[-1] + arr[i] - arr[i - 1] - 1)

        l, r = 0, len(prefix)
        while l < r:
            m = (l + r - 1) // 2
            if prefix[m] >= k:
                r = m
            else:
                l = m + 1
        # 若l=0，代表k本身就是小於arr[0]，所以直接回傳k即可
        # ex arr = [2], k = 1 -> 這個時候我們找到的 l 為0 代表k本身就是小於arr[0]
        # 所以應該回傳 0 + k  = k
        if l == 0:
            return k
        return arr[l - 1] + (k - prefix[l - 1])

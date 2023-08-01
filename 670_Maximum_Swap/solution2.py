class Solution:
    def maximumSwap(self, num: int) -> int:
        num_arr = [int(n) for n in str(num)]
        # 為什麼要取 last_idx?
        # 因為當交換時我們總是希望那一個數字的下標越大越好
        # 例如: 1991 -> 我們希望交換第二個 9 而不是第一個 9 -> 9911
        last_idx = [-1 for _ in range(10)]
        for i, v in enumerate(num_arr):
            last_idx[v] = i

        for i, v in enumerate(num_arr):
            for _num in range(9, v, -1):
                if last_idx[_num] != -1 and last_idx[_num] > i:
                    num_arr[last_idx[_num]], num_arr[i] = (
                        num_arr[i],
                        num_arr[last_idx[_num]],
                    )
                    return int("".join(str(n) for n in num_arr))
        return num

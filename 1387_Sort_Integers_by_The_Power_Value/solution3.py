import collections
import random


class Element:
    def __init__(self, num, step):
        self.num = num
        self.step = step

    def __lt__(self, other):
        if self.step == other.step:
            return self.num < other.num
        return self.step < other.step


class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        self.memo = collections.defaultdict(int)
        self.num_list = []
        for _num in range(lo, hi + 1):
            self.num_list.append(Element(_num, self.getStep(_num)))

        # 這裡我們要取 k-1，因為我們的 num_list 是從 0 開始的, 而題目的 k 是從 1 開始的
        self.quick_select(0, len(self.num_list) - 1, k - 1)
        elem = self.num_list[k - 1]
        return elem.num

    def getStep(self, num: int) -> int:
        if num == 1:
            return 1

        if num in self.memo.keys():
            return self.memo[num]

        if num % 2 == 0:
            return 1 + self.getStep(num // 2)
        else:
            return 1 + self.getStep(3 * num + 1)

    def quick_select(self, l, r, k):
        if l >= r:
            return
        mid = self.partition(l, r)
        if mid == k:
            return
        elif mid < k:
            self.quick_select(mid + 1, r, k)
        else:
            self.quick_select(l, mid - 1, k)

    def partition(self, l, r):
        pivot_idx = random.randint(l, r)
        pivot = self.num_list[pivot_idx]
        self.num_list[l], self.num_list[pivot_idx] = (
            self.num_list[pivot_idx],
            self.num_list[l],
        )
        while l < r:
            while l < r and self.num_list[r] > pivot:
                r -= 1
            self.num_list[l] = self.num_list[r]
            while l < r and self.num_list[l] < pivot:
                l += 1
            self.num_list[r] = self.num_list[l]
        self.num_list[l] = pivot
        return l

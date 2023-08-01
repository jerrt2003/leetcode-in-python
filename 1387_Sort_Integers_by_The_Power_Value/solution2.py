import collections
import heapq


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
        num_list = []
        for _num in range(lo, hi + 1):
            num_list.append(Element(_num, self.getStep(_num)))

        heapq.heapify(num_list)

        element = None
        while k > 0:
            element = heapq.heappop(num_list)
            k -= 1

        return element.num

    def getStep(self, num: int) -> int:
        if num == 1:
            return 1

        if num in self.memo.keys():
            return self.memo[num]

        if num % 2 == 0:
            return 1 + self.getStep(num // 2)
        else:
            return 1 + self.getStep(3 * num + 1)

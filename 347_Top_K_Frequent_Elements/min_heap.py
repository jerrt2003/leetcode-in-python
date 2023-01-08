import collections
import heapq

from typing import List

class Element:
    def __init__(self, val: int = None, count: int = None):
        self.val = val
        self.count = count

    def __lt__(self, other):
        if self.count == other.count:
            return self.val > other.val
        return self.count < other.count

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freq_map = collections.Counter(nums)
        elem_arr: List[Element] = []
        heapq.heapify(elem_arr)
        for key, value in freq_map.items():
            elem = Element(val=key, count=value)
            heapq.heappush(elem_arr, elem)
            if len(elem_arr) > k:
                heapq.heappop(elem_arr)
        ans: List[int] = []
        for elem in elem_arr:
            ans.append(elem.val)
        return ans
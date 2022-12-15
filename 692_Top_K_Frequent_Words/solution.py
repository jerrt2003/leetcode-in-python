import heapq
import collections

from typing import List, Tuple

class Element:
    def __init__(self, word, count):
        self.word: str = word
        self.count: int = count

    def __lt__(self, other):
        if self.count == other.count:
            # when retreiving the answer we need to make sure the word 
            # which has smaller lexicographical get popped first
            # as we'll reverse the ans at the end 
            return self.word > other.word
        return self.count < other.count

    def __eq__(self, other):
        return self.count == other.count and self.word == other.word

class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        # use Counter to provide counts for each words
        counter = collections.Counter(words)
        # here we maintain a 'min' heap
        pq: List[Element] = []
        heapq.heapify(pq)
        for word, count in counter.items():
            element = Element(word, count)
            heapq.heappush(pq, element)
            # when pq's len > k, we pop the 1st element from the pq 
            # as pq is a min heap, the smallest word will always 
            # get popped
            if len(pq) > k:
                heapq.heappop(pq)
        ans: List[str] = []
        while pq:
            ans.append(heapq.heappop(pq).word)
        return ans[::-1]




import collections
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        self.visited1 = collections.defaultdict(int)
        self.visited1[beginWord] = 1
        self.visited2 = collections.defaultdict(int)
        self.visited2[endWord] = 1
        self.q1, self.q2 = collections.deque([beginWord]), collections.deque([endWord])

        self.wordList = set(wordList)

        if endWord not in self.wordList:
            return 0

        while self.q1 and self.q2:
            if len(self.q1) > len(self.q2):
                ret = self.update(1)
            else:
                ret = self.update(0)
            if ret != -1:
                return ret

        return 0

    def update(self, type: int) -> int:
        q = self.q1 if type == 0 else self.q2
        q_len = len(q)
        for _ in range(q_len):
            cur_word = q.popleft()
            if (type == 0 and cur_word in self.visited2.keys()) or (
                type == 1 and cur_word in self.visited1.keys()
            ):
                return self.visited1[cur_word] + self.visited2[cur_word] - 1
            for next_word in self.find_next_words(cur_word):
                if type == 0 and next_word not in self.visited1.keys():
                    self.visited1[next_word] = self.visited1[cur_word] + 1
                    q.append(next_word)
                elif type == 1 and next_word not in self.visited2.keys():
                    self.visited2[next_word] = self.visited2[cur_word] + 1
                    q.append(next_word)
        return -1

    def find_next_words(self, word) -> List[str]:
        ret_list = []
        for candidate in self.wordList:
            diff_count = 0
            for i in range(len(word)):
                if candidate[i] != word[i]:
                    diff_count += 1
            if diff_count == 1:
                ret_list.append(candidate)

        return ret_list

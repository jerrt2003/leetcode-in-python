from typing import List

class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        # create a q and push init 'word'
        # convert 'wordList' to set for ref
        cur_level: int = 1
        self.q = [beginWord]
        self.visited = {beginWord}
        self.wordList = wordList

        # BFS
        # pop the 'word' from q, if 'word' == endWord, return current 'level'(i.e. dist)
        # if not, from remaining candidate find next available word lists
        # remove available words from 'wordList' set and push them into q
        # increase cur_level by 1
        while self.q:
            level_len = len(self.q)
            for _ in range(level_len):
                word = self.q.pop(0)
                if word == endWord:
                    return cur_level
                self.find_adjacent_words(word)
            cur_level += 1

        # return 0 (i.e. not found)
        return 0

    def find_adjacent_words(self, word: str) -> None:
        for candidate in self.wordList:
            if candidate not in self.visited:
                diff_count = 0
                for chr_1, chr_2 in zip(candidate, word):
                    if chr_1 != chr_2:
                        diff_count += 1
                if diff_count == 1:
                    self.visited.add(candidate)
                    self.q.append(candidate)
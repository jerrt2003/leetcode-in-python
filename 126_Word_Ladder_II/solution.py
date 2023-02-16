from typing import List

class WordInfo:
    def __init__(self, word: str = None, path: List = None):
        self.word = word
        self.path = path

class Solution:
    def findLadders(self, beginWord: str, endWord: str, wordList: List[str]) -> List[List[str]]:
        word = WordInfo(word=beginWord, path = [beginWord])
        q = [word]
        ans = []
        while len(q) != 0:
            n = len(q)
            for _ in range(n):
                word_info = q.pop(0)
                if word_info.word == endWord:
                    ans.append(word_info.path)
                else:
                    next_word_list = self.findNextWord(word_info, wordList)
                    q.extend(next_word_list)
            if len(ans) != 0:
                return ans
        return ans

    def findNextWord(self, word_info: "WordInfo", wordList: List[str]) -> List[WordInfo]:
        ret = []
        cur_word = word_info.word
        path_set = set(word_info.path)
        for word in wordList:
            if self.word_diff_by_one(cur_word, word) and word not in path_set:
                new_word_info = WordInfo(word=word, path=word_info.path+[word])
                ret.append(new_word_info)
        return ret
    
    def word_diff_by_one(self, word1: str, word2: str) -> bool:
        count = 0
        for w1, w2 in zip(word1, word2):
            if w1 != w2:
                count += 1
        return count == 1

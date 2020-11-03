import collections


class Solution(object):
    def ladderLength(self, beginWord, endWord, wordList):
        """
        Facebook
        T:O(m*n*26) S:O(n)
        Runtime: 416 ms, faster than 41.41% of Python online submissions for Word Ladder.
        Memory Usage: 13.7 MB, less than 88.62% of Python online submissions for Word Ladder.
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """
        chars = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'n', 'o', 'p', 'q', 'r', 's',
                 't', 'u', 'v', 'w', 'x', 'y', 'z']
        wordList = set(wordList)
        queue = collections.deque([beginWord])
        level = 0
        while queue:
            for _ in range(len(queue)):
                word = queue.popleft()
                if word == endWord:
                    return level
                else:
                    for i in range(len(word)):
                        for c in chars:
                            new_word = word[:i] + c + word[i + 1:]
                            if new_word in wordList:
                                wordList.remove(new_word)
                                queue.append(new_word)
            level += 1

        return 0


print Solution().ladderLength('hit','cog',["hot","dot","dog","lot","log","cog"])
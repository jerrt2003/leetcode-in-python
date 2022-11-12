# -*- coding: utf-8 -*-
class Solution(object):
    def wordsTyping(self, sentence, rows, cols):
        """
        :type sentence: List[str]
        :type rows: int
        :type cols: int
        :rtype: int
        """
        i = 1
        repeat = 0
        _sentence = sentence[:]
        curr_len = 0
        while i < rows+1:
            if i > 1 and _sentence[0] == sentence[0]:
                break
            else:
                if curr_len + len(_sentence[0]) >= cols:
                    curr_len = 0
                    i += 1
                elif curr_len + len(_sentence[0]) == cols-1:
                    curr_len = 0
                    i += 1
                    _sentence.pop(0)
                    if not _sentence:
                        repeat += 1
                        _sentence = sentence[:]
                else:
                    curr_len = curr_len + len(_sentence[0]) + 1
                    _sentence.pop(0)
                    if not _sentence:
                        repeat += 1
                        _sentence = sentence[:]
        return rows / (i-1) * repeat





sentence = ["Two", "consecutive", "words", "in", "a", "line", "must" ,"be", "separated", "by", "a", "single", "space"]
row = 20000
col = 20000
print Solution().wordsTyping(sentence, row, col)


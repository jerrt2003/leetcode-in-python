# -*- coding: utf-8 -*-
class Solution(object):
    def wordsTyping(self, sentence, rows, cols):
        """
        :type sentence: List[str]
        :type rows: int
        :type cols: int
        :rtype: int
        """
        idx, span, curr_len, repeat = 0, 0, 0, 0
        while span < rows:
            if idx == 0 and curr_len == 0 and span > 0:
                # pattern found, but we need to deal with remain rows
                remain_rows = rows % span
                idx, _span, curr_len, _repeat = 0, 0, 0, 0
                while _span < remain_rows:
                    if curr_len + len(sentence[idx]) <= cols:
                        curr_len = curr_len + len(sentence[idx]) + 1
                        idx += 1
                    else:
                        curr_len = 0
                        _span += 1
                    if idx == len(sentence):
                        _repeat += 1
                        idx = 0
                return rows/span*repeat + _repeat
            if curr_len + len(sentence[idx]) <= cols:
                curr_len = curr_len + len(sentence[idx]) + 1
                idx += 1
            else:
                curr_len = 0
                span += 1
            if idx == len(sentence):
                repeat += 1
                idx = 0
        if repeat == 0:
            return 0
        else:
            return repeat

sentence = ["hello","world"]
rows = 2
cols = 8
assert Solution().wordsTyping(sentence, rows, cols) == 1

rows = 3
cols = 6
sentence = ["a", "bcd", "e"]
assert Solution().wordsTyping(sentence, rows, cols) == 2

rows = 4
cols = 5
sentence = ["I", "had", "apple", "pie"]
assert Solution().wordsTyping(sentence, rows, cols) == 1

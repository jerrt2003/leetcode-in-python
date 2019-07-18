# -*- coding: utf-8 -*-
class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        res, cur, num_of_char = [], [], 0
        for w in words:
            if num_of_char + len(w) + len(cur) > maxWidth:
                for i in range(maxWidth - num_of_char):
                    cur[i % (len(cur)-1 or 1)] += ' '
                res.append(''.join(cur))
                num_of_char, cur = 0, []
            cur.append(w)
            num_of_char += len(w)
        return res + [' '.join(cur).ljust(maxWidth)]

words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16
assert Solution().fullJustify(words, maxWidth) == [
   "This    is    an",
   "example  of text",
   "justification.  "
]

words = ["What","must","be","acknowledgment","shall","be"]
maxWidth = 16
assert Solution().fullJustify(words, maxWidth) == [
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]

words = ["Science","is","what","we","understand","well","enough","to","explain",
         "to","a","computer.","Art","is","everything","else","we","do"]
maxWidth = 20
assert Solution().fullJustify(words, maxWidth) == [
  "Science  is  what we",
  "understand      well",
  "enough to explain to",
  "a  computer.  Art is",
  "everything  else  we",
  "do                  "
]

words = ["ask","not","what","your","country","can","do","for","you","ask","what","you","can","do","for","your","country"]
maxWidth = 16
assert Solution().fullJustify(words, maxWidth) == ["ask   not   what","your country can","do  for  you ask","what  you can do","for your country"]


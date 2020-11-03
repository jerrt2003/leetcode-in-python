# -*- coding: utf-8 -*-
class Solution(object):
    def fullJustify(self, words, maxWidth):
        """
        T: O(n)
        S: O(n)
        Perf: Runtime: 24 ms, faster than 27.82% / Memory Usage: 11.7 MB, less than 86.80%
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """
        res = []
        wordsSoFar = []
        currLen = 0
        idx = 0
        while idx < len(words):
            currLen += len(words[idx])
            if currLen <= maxWidth:
                wordsSoFar.append(words[idx])
                currLen += 1
                idx += 1
            else:
                totalWordsLen = sum([len(w) for w in wordsSoFar])
                totalPadding = maxWidth - totalWordsLen
                if len(wordsSoFar) == 1:
                    output = wordsSoFar[0] + ' '*totalPadding
                else:
                    eachPadding = totalPadding / (len(wordsSoFar)-1)
                    extraPadding = totalPadding % (len(wordsSoFar)-1)
                    output = ''
                    count = 0
                    pads_count = 0
                    while count < len(wordsSoFar):
                        if count == len(wordsSoFar)-1:
                            output += wordsSoFar[count]
                        else:
                            output += wordsSoFar[count]
                            output += ' '*eachPadding
                            if pads_count < extraPadding:
                                output += ' '
                                pads_count += 1
                        count += 1
                res.append(output)
                currLen = 0
                wordsSoFar = []
        if wordsSoFar:
            totalWordsLen = sum([len(w) for w in wordsSoFar])
            totalPadding = maxWidth - totalWordsLen
            if len(wordsSoFar) == 1:
                output = wordsSoFar[0] + ' ' * totalPadding
            else:
                output = ''
                for w in wordsSoFar:
                    output += w
                    if totalPadding > 0:
                        output += ' '
                        totalPadding -= 1
                if totalPadding > 0:
                    output += ' '*totalPadding
            res.append(output)
        return res

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

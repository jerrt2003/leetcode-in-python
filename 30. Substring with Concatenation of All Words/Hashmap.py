# -*- coding: utf-8 -*-
from hash2 import Counter
class Solution(object):
    def findSubstring(self, s, words):
        """
        Solution: 2 dict(hashmap) solution
        Time Complexity: O(m*n)
        Space Complexity: O(m)
        Inspired By: https://leetcode.windliang.cc/leetCode-30-Substring-with-Concatenation-of-All-Words.html
        TP:
        - first based on 'words' we build a dict <k, v> = <words, words count>
        - Then we go through target 's'
            - in each iteration we first copy the dict
            - then we check the sub-string to check if word existed or not
            - if yes we decrease the count
            - if not then we break the loop (means this sub-string contains non-candidate word)
        - Finally we check the copied dict to see if all key has value 0
            - if yes which means we had a valid sub-string
            - if not means we don't, move on to next iteration
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """
        if words is None or len(words) == 0: return []
        words_dict = dict(Counter(words)) # !!! Use Counter class to speed up the list -> dict process
        single_word_length = len(words[0])
        res = []
        for i in range(0, len(s)-single_word_length*len(words)+1):
            words_so_far = words_dict.copy()
            for j in range(i, i+single_word_length*len(words), single_word_length):
                _tmp = s[j:j+single_word_length]
                if _tmp in words_so_far:
                    words_so_far[_tmp] -= 1
                    if words_so_far[_tmp] < 0:
                        break
                else:
                    break
            has_match = True
            for v in words_so_far.values():
                if v != 0:
                    has_match = False
                    break
            if has_match:
                res.append(i)
        return res

#s = 'barfoothefoobarman'
s = 'aarfoothecoobarman'
s = ''
#words = ["foo","bar"]
words = []

print Solution().findSubstring(s, words)
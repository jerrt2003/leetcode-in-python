# -*- coding: utf-8 -*-
import hash2
import pq
class AutocompleteSystem(object):

    def __init__(self, sentences, times):
        """
        Solution: HashMap
        Time Complexity:
        Space Complexity:
        Perf: Runtime: 1888 ms, faster than 5.00% / Memory Usage: 13.5 MB, less than 100.00%
        :type sentences: List[str]
        :type times: List[int]
        """
        self.history = hash2.defaultdict(dict)
        for k, v in zip(sentences, times):
            self.history[k] = v
        self.search = []

    def input(self, c):
        """
        :type c: str
        :rtype: List[str]
        """
        if c == '#':
            key = ''.join(self.search)
            if key in self.history.keys():
                self.history[''.join(self.search)] += 1
            else:
                self.history[key] = 1
            self.search = []
            return []
        else:
            self.search.append(c)
            key = ''.join(self.search)
            res = []
            for k, v in self.history.iteritems():
                if k.startswith(key):
                    res.append((k, v))
            res.sort(key=lambda x: x[1], reverse=True)
            return self.processData(res)

    def processData(self, data):
        tmp = dict()
        keys = []
        for k, v in data:
            if v in tmp.keys():
                tmp[v].append(k)
            else:
                tmp[v] = [k]
                keys.append(v)
        res = []
        while len(res) < 3 and keys:
            _k = keys.pop(0)
            word_list = tmp[_k]
            word_list.sort()
            while len(res) < 3 and word_list:
                res.append(word_list.pop(0))
        return res

# Your AutocompleteSystem object will be instantiated and called as such:
# obj = AutocompleteSystem(sentences, times)
# param_1 = obj.input(c)
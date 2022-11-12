import collections


class StreamChecker(object):

    def __init__(self, words):
        """
        :type words: List[str]
        """
        self.root = TrieNode()
        for word in words:
            root = self.root
            for w in word[::-1]:
                if w not in root.children:
                    newNode = TrieNode(c=w)
                    root.children[w] = newNode
                root = root.children[w]
            root.isEnd = True
        self.path = collections.deque([])

    def query(self, letter):
        """
        :type letter: str
        :rtype: bool
        """
        self.path.appendleft(letter)
        root = self.root
        for p in self.path:
            if p not in root.children:
                return False
            root = root.children[p]
            if root.isEnd:
                return True
        return False


class TrieNode(object):
    def __init__(self, c=None):
        self.c = c
        self.children = dict()
        self.isEnd = False

# Your StreamChecker object will be instantiated and called as such:
# obj = StreamChecker(words)
# param_1 = obj.query(letter)
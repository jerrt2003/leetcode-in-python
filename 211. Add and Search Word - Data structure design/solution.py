class WordDictionary(object):

    def __init__(self):
        """
        Facebook
        Trie
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word):
        """
        T:O(n) n: len of word
        Adds a word into the data structure.
        :type word: str
        :rtype: None
        """
        node = self.root
        for w in word:
            if w not in node.childs:
                new_node = TrieNode(c=w)
                node.childs[w] = new_node
            node = node.childs[w]
        node.isEnd = True

    def search(self, word):
        """
        T:O(n)
        Returns if the word is in the data structure. A word could contain the dot character '.' to represent any one letter.
        :type word: str
        :rtype: bool
        """
        word = [w for w in word]

        def dfs(node, i):
            if i == len(word):
                return node.isEnd
            if word[i] == ".":
                return any(dfs(nxt, i + 1) for nxt in node.childs.values())
            elif word[i] not in node.childs:
                return False
            else:
                return dfs(node.childs[word[i]], i + 1)

        return dfs(self.root, 0)


class TrieNode(object):
    def __init__(self, c=None):
        self.c = c
        self.childs = dict()
        self.isEnd = False

# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)



obj = WordDictionary()
obj.addWord('bad')
obj.addWord('dad')
obj.addWord('mad')
# obj.search('bad')
print obj.search('.ad')
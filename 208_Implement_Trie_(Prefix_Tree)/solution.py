from typing import Dict

class TreeNode:
    def __init__(self, chr: str = None):
        """TreeNode data structure should contains:
        1. character
        2. children which is a dict of charater:TreeNode
        3. is_end: bool which inidicate if this is a complete word

        Args:
            chr (str, optional): character. Defaults to None.
        """
        self.w: str = chr
        self.children: Dict[str, TreeNode] = {}
        self.is_end: bool = False

class Trie:

    def __init__(self):
        self.root = TreeNode()
        

    def insert(self, word: str) -> None:
        root = self.root
        for w in word:
            if w not in root.children.keys():
                node = TreeNode(chr=w)
                root.children[w] = node
            root = root.children[w]
        root.is_end = True

    def search(self, word: str) -> bool:
        root = self.root
        for w in word:
            if w not in root.children.keys():
                return False
            root = root.children[w]
        return root.is_end

    def startsWith(self, prefix: str) -> bool:
        root = self.root
        for w in prefix:
            if w not in root.children.keys():
                return False
            root = root.children[w]
        return True

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)
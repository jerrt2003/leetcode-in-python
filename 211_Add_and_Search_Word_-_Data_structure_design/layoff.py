from typing import Dict


class TreeNode:
    def __init__(self, w: str = None):
        self.w = w
        self.children: Dict[str, TreeNode] = {}
        self.is_end = False

class WordDictionary:

    def __init__(self):
        self.root = TreeNode()
        
    def addWord(self, word: str) -> None:
        node = self.root
        for w in word:
            if w not in node.children.keys():
                child = TreeNode(w=w)
                node.children[w] = child
            node = node.children[w]
        node.is_end = True

    def search(self, word: str) -> bool:
        def dfs(node: TreeNode, i: int) -> bool:
            if i == len(word):
                return node.is_end
            if word[i] == ".":
                return any(dfs(nxt_node, i+1) for nxt_node in node.children.values())
            elif word[i] not in node.children.keys():
                return False
            else:
                return dfs(node.children[word[i]], i+1)
        
        return dfs(self.root, 0)
        


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)
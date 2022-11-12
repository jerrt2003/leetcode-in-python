class Solution(object):
    def removeSubfolders(self, folder):
        """
        Trie
        T:O(n) S:O(n)
        Runtime: 492 ms, faster than 17.32% of Python online submissions for Remove Sub-Folders from the Filesystem.
        Memory Usage: 62.6 MB, less than 100.00% of Python online submissions for Remove Sub-Folders from the Filesystem.
        :type folder: List[str]
        :rtype: List[str]
        """
        trie = Trie()
        for f in folder:
            trie.addFolder(f)

        trie.dfs(trie.root, "")
        return trie.folder

class Trie(object):
    def __init__(self):
        self.root = TrieNode(char="")
        self.folder = []

    def addFolder(self, folder):
        root = self.root
        for f in folder.split('/')[1:]:
            if f not in root.children:
                node = TrieNode(char=f)
                root.children[f] = node
                root = node
            else:
                root = root.children[f]
        root.isEnd = True

    def dfs(self, node, path):
        if node.isEnd:
            self.folder.append(path + '/' + node.char)
        else:
            for _, next_node in node.children.iteritems():
                if not node.char:
                    self.dfs(next_node, path)
                else:
                    self.dfs(next_node, path + '/' + node.char)


class TrieNode(object):
    def __init__(self, char=None):
        self.char = char
        self.children = dict()
        self.isEnd = False


print Solution().removeSubfolders(["/a","/a/b","/c/d","/c/d/e","/c/f"])
print Solution().removeSubfolders(["/a","/a/b/c","/a/b/d"])

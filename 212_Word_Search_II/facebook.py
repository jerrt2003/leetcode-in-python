class Solution(object):
    def findWords(self, board, words):
        """
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        root = TrieNode()
        for word in words:
            node = root
            for w in word:
                if w not in node.children:
                    new_node = TrieNode(w)
                    node.children[w] = new_node
                node = node.children[w]
            node.isEnd = True
            node.word = word

        ans = []
        m, n = len(board), len(board[0])

        def dfs(node, path, i, j):
            if node.isEnd:
                ans.append(node.word)
                # return
            for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if 0 <= x < m and 0 <= y < n and (x, y) not in path and board[x][y] in node.children:
                    dfs(node.children[board[x][y]], path + [(x, y)], x, y)

        for i in range(m):
            for j in range(n):
                if board[i][j] in root.children:
                    dfs(root.children[board[i][j]], [(i, j)], i, j)

        return ans


class TrieNode(object):
    def __init__(self, c=None):
        self.c = c
        self.children = dict()
        self.isEnd = False
        self.word = None


print Solution().findWords([["o","a","a","n"],["e","t","a","e"],["i","h","k","r"],["i","f","l","v"]], ["oath","pea","eat","rain"])
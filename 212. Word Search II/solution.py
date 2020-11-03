class Solution(object):
    def findWords(self, board, words):
        """
        Facebook
        T:O(m*n*(4*3^L-1)) S:O(n) (n == total number of letters in dict)
        Runtime: 400 ms, faster than 64.35% of Python online submissions for Word Search II.
        Memory Usage: 48.6 MB, less than 51.50% of Python online submissions for Word Search II.
        :type board: List[List[str]]
        :type words: List[str]
        :rtype: List[str]
        """
        self.root = TrieNode()

        # build Trie
        for word in words:
            root = self.root
            for w in word:
                if w not in root.children:
                    new_node = TrieNode(w)
                    root.children[w] = new_node
                root = root.children[w]
            root.isEnd = True

        m, n = len(board), len(board[0])
        ans = set()

        def dfs(i, j, path, node):
            if node.isEnd:
                ans.add(''.join([board[a][b] for a, b in path]))
                # return
            for x, y in [(i - 1, j), (i + 1, j), (i, j - 1), (i, j + 1)]:
                if 0 <= x < m and 0 <= y < n and (x, y) not in path and board[x][y] in node.children:
                    dfs(x, y, path + [(x, y)], node.children[board[x][y]])

        for i in range(m):
            for j in range(n):
                if board[i][j] in self.root.children:
                    dfs(i, j, [(i, j)], self.root.children[board[i][j]])

        return list(ans)


class TrieNode(object):
    def __init__(self, c=None):
        self.c = c
        self.children = dict()
        self.isEnd = False
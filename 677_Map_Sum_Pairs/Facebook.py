class MapSum(object):

    def __init__(self):
        """
        Facebook
        Trie
        Runtime: 8 ms, faster than 100.00% of Python online submissions for Map Sum Pairs.
        Memory Usage: 12.9 MB, less than 21.31% of Python online submissions for Map Sum Pairs.
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, key, val):
        """
        T:O(n)
        :type key: str
        :type val: int
        :rtype: None
        """
        node = self.root
        for k in key:
            if k not in node.child:
                new_node = TrieNode(c=k)
                node.child[k] = new_node
            node = node.child[k]
        node.isEnd = True
        node.val = val

    def sum(self, prefix):
        """
        T:O(n)
        :type prefix: str
        :rtype: int
        """

        def dfs(node):
            ans = 0
            if node.isEnd:
                ans += node.val
            for k in node.child:
                ans += dfs(node.child[k])
            return ans

        node = self.root
        for p in prefix:
            if p not in node.child:
                return 0
            node = node.child[p]
        return dfs(node)


class TrieNode(object):
    def __init__(self, c=None, val=None):
        self.c = c
        self.val = val
        self.child = dict()
        self.isEnd = False

# Your MapSum object will be instantiated and called as such:
# obj = MapSum()
# obj.insert(key,val)
# param_2 = obj.sum(prefix)
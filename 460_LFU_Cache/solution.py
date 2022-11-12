import collections


class LFUCache(object):

    def __init__(self, capacity):
        """
        Facebook
        Runtime: 296 ms, faster than 45.23% of Python online submissions for LFU Cache.
        Memory Usage: 23.4 MB, less than 15.77% of Python online submissions for LFU Cache.
        :type capacity: int
        """
        self.cap = capacity
        self.key2node = dict()
        self.count2nodes = collections.defaultdict(collections.OrderedDict)
        self.minCont = None

    def get(self, key):
        """
        T:O(1)
        :type key: int
        :rtype: int
        """
        # if key not in cache, return -1
        if key not in self.key2node:
            return -1
        # get node
        node = self.key2node[key]
        # remove this node from the corresponding node.count dict
        del self.count2nodes[node.count][key]
        # clean memory
        if not self.count2nodes[node.count]:
            del self.count2nodes[node.count]
        # update node.count
        node.count += 1
        # adding node to the node.count ordered dict
        self.count2nodes[node.count][key] = node
        # if count2nodes minCont has no nodes, increase minCont
        if not self.count2nodes[self.minCont]:
            self.minCont += 1
        return node.v

    def put(self, key, value):
        """
        T:O(1)
        :type key: int
        :type value: int
        :rtype: None
        """
        if not self.cap:
            return
        if key in self.key2node:
            # update node.val and node.nodeCnt
            self.key2node[key].v = value
            self.get(key)
            return
        # if over the cap, remove last frequent node
        if len(self.key2node) == self.cap:
            k, _ = self.count2nodes[self.minCont].popitem(last=False) # FIFO
            del self.key2node[k]
        # create new node
        self.count2nodes[1][key] = self.key2node[key] = Node(key, value)
        self.minCont = 1


class Node(object):
    def __init__(self, k, v):
        self.k = k
        self.v = v
        self.count = 1


# Your LFUCache object will be instantiated and called as such:
# obj = LFUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
import heapq


class Node:
    def __init__(self, char: str = None, count: int = None):
        self.char = char
        self.count = count

    def __lt__(self, other):
        return self.count > other.count


class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        # 先创建一个包含三个节点的列表，然后使用heapq.heapify(q)将其转化为堆。
        # 其中每个节点都包含一个字符（'a'、'b'或'c'）和对应的个数。
        q = [Node("a", a), Node("b", b), Node("c", c)]
        heapq.heapify(q)
        ans = ""
        tmp_node = None
        # 然后进入主循环，不断从堆中取出当前剩余个数最多的字符对应的节点。
        while len(q) != 0:
            node = heapq.heappop(q)
            # 判断当前取出的节点的字符个数是否为0，如果为0，那么这个字符已经用完，无法再使用，直接跳过本次循环。
            if node.count == 0:
                continue
            # 判断当前取出的节点的字符是否与生成的字符串的最后两个字符相同，如果相同，
            # 那么按照题目的规定，不能再使用这个字符，将这个节点暂时保存在tmp_node变量中，然后跳过本次循环。
            if len(ans) >= 2 and ans[-2] == node.char and ans[-1] == node.char:
                tmp_node = node
                continue
            # 将当前节点的字符添加到生成的字符串中，并将当前节点的字符个数减1，然后将当前节点再次放回堆中。
            ans += node.char
            node.count -= 1
            heapq.heappush(q, node)
            # 最后，如果tmp_node不为空，那么说明之前有一个节点因为字符连续出现两次而暂时不能使用，
            # 现在已经使用了其他的字符，可以再次使用这个字符了，所以将这个节点再次放回堆中。
            if tmp_node:
                heapq.heappush(q, tmp_node)
                tmp_node = None
        return ans

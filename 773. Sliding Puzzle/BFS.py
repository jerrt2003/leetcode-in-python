# -*- coding: utf-8 -*-
class Solution(object):
    def slidingPuzzle(self, board):
        """
        Solution: BFS
        Time Complexity:
        Space Complexity:
        Inspired By: https://leetcode.com/problems/sliding-puzzle/discuss/146652/Java-8ms-BFS-with-algorithm-explained
        TP:
        - Consider each state in the board as a graph node, we just need to find out the min distance between start node
        and final target node "123450". Since it's a single point to single point questions, Dijkstra is not needed here.
        We can simply use BFS, and also count the level we passed.
        Every time we swap 0 position in the String to find the next state. Use a hashTable to store the visited states.
        :type board: List[List[int]]
        :rtype: int
        """
        target = [1,2,3,4,5,0]
        start = board[0]+board[1]
        q = [start]
        visited = set(tuple(start)) # By using SET we can speed up the search in visited
        res = 0
        dir_options = [[1,3],[0,2,4],[1,5],[0,4],[1,3,5],[2,4]]
        # !!! WHY? when zero is in position:0 it can go to cell {1,3},
        # position:1 it can go {0,2,4} and so on,
        while q:
            for _ in range(len(q)):
                curr_state = q.pop(0)
                if curr_state == target:
                    return res
                else:
                    zero_pos = curr_state.index(0)
                    for i in dir_options[zero_pos]:
                        _tmp = curr_state[:]
                        _tmp[i], _tmp[zero_pos] = _tmp[zero_pos], _tmp[i]
                        if not tuple(_tmp) in visited:
                            visited.add(tuple(_tmp)) # WHY we need to add visited --> 假設這個組合已經在之前就看過了表示現在在加進去的話他的res一定會比較大,所以加進去沒意義
                            q.append(_tmp)
            res += 1
        return -1

board = [[1,2,3],[4,0,5]]
print Solution().slidingPuzzle(board)
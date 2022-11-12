# -*- coding: utf-8 -*-
import heapq
class GoogleInterview(object):
    """
    原题：一组坐标表示人，另一组表示车，车比人多，给每个人匹配最近的车。其中人和车的距离没有tie。
    原题还比较简单，最笨的bfs也可以做，坐标数值很大的时候，时间复杂度可能会很高，稍微好一点的是用pq存所有的人车距离，
    每次poll最小的距离，如果这个人已经匹配到车了继续poll，直到所有人都匹配到车为止
    原题不难，用一个heap和visit就可以解决.
    people: [[1,1],[2,3],[4,1],[5,2]]
    cars: [[2,1],[2,2],[6,4],[1,3],[7,3]]
    """
    def Solution(self, people, cars):
        res = dict()

        def dist(a, b):
            return abs(a[0]-b[0]) + abs(a[1]-b[1])

        pq = []
        for i, p in enumerate(people):
            for j, c in enumerate(cars):
                heapq.heappush(pq, (dist(p, c), i, j))

        visit_p = set()
        visit_c = set()
        while len(res) < len(people):
            cand = heapq.heappop(pq)
            p, c = cand[1], cand[1]
            if p in visit_p or c in visit_c:
                continue
            visit_p.add(p)
            visit_c.add(c)
            res[p] = c
        return res

print GoogleInterview().Solution([[1,1],[2,3],[4,1],[5,2]], [[2,1],[2,2],[6,4],[1,3],[7,3]])
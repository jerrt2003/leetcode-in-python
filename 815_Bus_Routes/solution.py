import collections
from typing import List


class Solution:
    def numBusesToDestination(
        self, routes: List[List[int]], source: int, target: int
    ) -> int:
        if source == target:
            return 0
        # key: stop_idx, values: list of route_idx
        # 代表該站有哪些路線可以到達
        stop_to_route_maps = collections.defaultdict(list)
        for route_idx, route in enumerate(routes):
            for stop in route:
                stop_to_route_maps[stop].append(route_idx)

        visited = set()
        q = collections.deque()

        for route_idx in stop_to_route_maps[source]:
            visited.add(route_idx)
            q.append(route_idx)

        ans = 0
        while q:
            ans += 1
            l = len(q)
            for _ in range(l):
                # 每次我們 pop出一個 route_idx
                route_idx = q.popleft()
                # 然後檢查該路線上的每一個站
                for stop in routes[route_idx]:
                    # 假如該站是我們要找的終點 就回傳答案
                    if stop == target:
                        return ans
                    # 否則檢查該站有哪些路線可以到達 若該路線尚未被拜訪過(搭乘) 就加入q中 並且標記為已拜訪
                    for nxt_route_idx in stop_to_route_maps[stop]:
                        if nxt_route_idx not in visited:
                            visited.add(nxt_route_idx)
                            q.append(nxt_route_idx)

        return -1

import heapq
from typing import List


class Stop:
    def __init__(self, passenger_count: int, trip_end: int):
        self.passenger_count = passenger_count
        self.trip_end = trip_end

    def __lt__(self, other):
        return self.trip_end < other.trip_end


class Solution:
    def carPooling(self, trips: List[List[int]], capacity: int) -> bool:
        # 將行程根據起始地點排序
        trips.sort(key=lambda x: x[1])
        ongoing_trips = []  # 使用heap存放正在進行的行程
        for passenger_count, trip_start, trip_end in trips:
            # 若有行程結束且行程結束地點在當前行程起始地點之前或同地，則將該行程乘客數加回總容量
            while ongoing_trips and trip_start >= ongoing_trips[0].trip_end:
                capacity += heapq.heappop(ongoing_trips).passenger_count
            # 若加入新行程後的乘客數不超過總容量，則將該行程加入進行中的行程，並將新行程的乘客數從總容量中扣除
            if capacity - passenger_count >= 0:
                heapq.heappush(ongoing_trips, Stop(passenger_count, trip_end))
                capacity -= passenger_count
            else:
                return False
        return True

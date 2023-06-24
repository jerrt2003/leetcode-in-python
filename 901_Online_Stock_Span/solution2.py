from typing import List

class Stock:
    def __init__(self, price, span):
        self.price = price
        self.span = span


class StockSpanner:

    def __init__(self):
        self.stack: List[Stock] = []

    def next(self, price: int) -> int:
        span = 1
        while self.stack and price >= self.stack[-1].price:
            prev_stock = self.stack.pop()
            span += prev_stock.span
        stock = Stock(price, span)
        self.stack.append(stock)
        return span
        



# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)
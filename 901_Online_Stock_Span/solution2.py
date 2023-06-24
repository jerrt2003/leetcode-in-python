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

# 當然可以。我們透過一組例子，來說明 StockSpanner 的 next 方法如何運作：

# spanner = StockSpanner()
# 首先，我們創建一個 StockSpanner 的實例 spanner，這個實例有一個名為 stack 的空堆疊。

# span = spanner.next(100)  # 返回 1
# 然後，我們將股票價格 100 傳入 next 方法。由於堆疊是空的，所以當天的股票跨度值為 1。我們創建一個 Stock 的實例，其 price 為 100，span 為 1，並將其推入堆疊。

# span = spanner.next(80)  # 返回 1
# 接著，我們將股票價格 80 傳入 next 方法。由於 80 小於堆疊頂部的股票價格 100，所以當天的股票跨度值為 1。我們創建一個 Stock 的實例，其 price 為 80，span 為 1，並將其推入堆疊。

# span = spanner.next(60)  # 返回 1
# 然後，我們將股票價格 60 傳入 next 方法。同樣的，由於 60 小於堆疊頂部的股票價格 80，所以當天的股票跨度值為 1。我們創建一個 Stock 的實例，其 price 為 60，span 為 1，並將其推入堆疊。

# span = spanner.next(70)  # 返回 2
# 接著，我們將股票價格 70 傳入 next 方法。這時，由於 70 大於堆疊頂部的股票價格 60，我們從堆疊中取出該 Stock 實例，並將其跨度值 1 加到當天的股票跨度值上，得到 2。我們創建一個 Stock 的實例，其 price 為 70，span 為 2，並將其推入堆疊。

# span = spanner.next(60)  # 返回 1
# 然後，我們將股票價格 60 傳入 next 方法。由於 60 小於堆疊頂部的股票價格 70，所以當天的股票跨度值為 1。我們創建一個 Stock 的實例，其 price 為 60，span 為 1，並將其推入堆疊。

# span = spanner.next(75)  # 返回 4
# 最後，我們將股票價格 75 傳入 next 方法。這時，由於 75 大於堆疊頂部的股票價格 60，我們從堆疊中取出該 Stock 實例，並將其跨度值 1 加到當天的股票跨度值上，得到 2。由於 75 仍然大於現在堆疊頂部的股票價格 70，我們同樣將該 Stock 實例取出，並將其跨度值 2 加到當天的股票跨度值上，得到 4。我們創建一個 Stock 的實例，其 price 為 75，span 為 4，並將其推入堆疊。
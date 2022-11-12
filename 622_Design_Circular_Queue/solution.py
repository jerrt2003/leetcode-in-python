class MyCircularQueue(object):

    def __init__(self, k):
        """
        Facebook
        Array
        Runtime: 76 ms, faster than 32.30% of Python online submissions for Design Circular Queue.
        Memory Usage: 13 MB, less than 77.17% of Python online submissions for Design Circular Queue.
        Initialize your data structure here. Set the size of the queue to be k.
        :type k: int
        """
        self.size = 0
        self.cap = k
        self.queue = [-1] * k
        self.front = self.back = 0

    def enQueue(self, value):
        """
        T:O(1)
        Insert an element into the circular queue. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False
        self.queue[self.front] = value
        self.front = (self.front + 1) % self.cap
        self.size += 1
        return True

    def deQueue(self):
        """
        T:O(1)
        Delete an element from the circular queue. Return true if the operation is successful.
        :rtype: bool
        """
        if self.isEmpty():
            return False
        self.queue[self.back] = -1
        self.back = (self.back + 1) % self.cap
        self.size -= 1
        return True

    def Front(self):
        """
        T:O(1)
        Get the front item from the queue.
        :rtype: int
        """
        return self.queue[self.back]

    def Rear(self):
        """
        T:O(1)
        Get the last item from the queue.
        :rtype: int
        """
        return self.queue[self.front - 1]

    def isEmpty(self):
        """
        T:O(1)
        Checks whether the circular queue is empty or not.
        :rtype: bool
        """
        return self.size == 0

    def isFull(self):
        """
        T:O(1)
        Checks whether the circular queue is full or not.
        :rtype: bool
        """
        return self.size == self.cap

# Your MyCircularQueue object will be instantiated and called as such:
# obj = MyCircularQueue(k)
# param_1 = obj.enQueue(value)
# param_2 = obj.deQueue()
# param_3 = obj.Front()
# param_4 = obj.Rear()
# param_5 = obj.isEmpty()
# param_6 = obj.isFull()
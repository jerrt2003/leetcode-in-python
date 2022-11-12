from random import random


class RandomizedSet(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.nums = dict()
        self.numsList = []

    def insert(self, val):
        """
        T:O(1)
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        if val not in self.nums:
            self.numsList.append(val)
            self.nums[val] = len(self.numsList) - 1
            return True
        return False

    def remove(self, val):
        """
        T:O(1)
        Removes a value from the set. Returns true if the set contained the specified element.
        :type val: int
        :rtype: bool
        """
        if val in self.nums:
            idx = self.nums[val]
            last_val = self.numsList[-1]
            self.nums[last_val] = idx
            self.numsList[idx], self.numsList[-1] = self.numsList[-1], self.numsList[idx]
            self.numsList.pop()
            del self.nums[val]
            return True
        return False

    def getRandom(self):
        """
        T:O(1)
        Get a random element from the set.
        :rtype: int
        """
        return random.choice(self.numsList)

# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()
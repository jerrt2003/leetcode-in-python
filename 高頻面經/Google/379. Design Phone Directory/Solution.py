class PhoneDirectory(object):

    def __init__(self, maxNumbers):
        """
        Initialize your data structure here
        @param maxNumbers - The maximum numbers that can be stored in the phone directory.
        :type maxNumbers: int
        """

        self.unassigned = range(maxNumbers)
        self.assigned = set()

    def get(self):
        """
        Provide a number which is not assigned to anyone.
        @return - Return an available number. Return -1 if none is available.
        :rtype: int
        """
        if not self.unassigned:
            return -1
        x = self.unassigned.pop(0)
        self.assigned.add(x)
        return x

    def check(self, number):
        """
        Check if a number is available or not.
        :type number: int
        :rtype: bool
        """
        if number in self.assigned:
            return False
        return True

    def release(self, number):
        """
        Recycle or release a number.
        :type number: int
        :rtype: None
        """
        if number in self.assigned:
            self.assigned.remove(number)
            self.unassigned.append(number)
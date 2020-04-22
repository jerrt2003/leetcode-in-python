# -*- coding: utf-8 -*-
class TextBox(object):
    def __init__(self, s, sign, right=None, below=None):
        self.right = right
        self.below = below
        self.sign = sign
        self.s = s

    def show(self):
        print(self.sign * 20)
        if self.right:
            print(self.sign + ' ' + self.s + ' ' * self.right + self.sign)
        elif self.below:
            print(self.sign + ' ' + self.s + ' ' + self.sign)
            for i in range(self.below):
                print(self.sign + ' '*(len(self.s) + 2) + self.sign)
        else:
            print(self.sign + ' ' + self.s + ' ' + self.sign)
        print(self.sign * 20)

    def paddedRight(self, offset):
        return TextBox(self.s, self.sign, right=offset)

    def paddedBelow(self, offset):
        return TextBox(self.s, self.sign, below=offset)


test = TextBox('test 123', '+')
test.show()
test.paddedBelow(3).show()
test.show()
test.paddedRight(10).show()
test.show()
__author__ = 'dcheng'
class Solution:
    # @param {string} s
    # @return {boolean}
    def isValid(self, s):
        set1 = {'{', '[', '(', '<'}
        set2 = {'}', ']', ')', '>'}
        charList = []
        for char in s:
            if len(charList) == 0 and char in set2:
                return False
            if char in set1:
                charList.append(char)
            else:
                if char == '}':
                    if charList.pop() != '{':
                        return False
                if char == '>':
                    if charList.pop() != '<':
                        return False
                if char == ']':
                    if charList.pop() != '[':
                        return False
                if char == ')':
                    if charList.pop() != '(':
                        return False
        if len(charList) != 0:
            return False
        return True
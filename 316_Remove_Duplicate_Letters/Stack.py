class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        Solution: Stack
        Time Complexity: O(n)
        Space Complexity: O(n)
        Inspired By: https://leetcode.com/problems/remove-duplicate-letters/discuss/76762/Java-O(n)-solution-using-stack-with-detail-explanation
        TP:
        - the basic idea is to use a stack to store 'added' characters and continue to compare the current character to the ones in the stack.
        Once we found if the current one has samller ord(), then we remove the top of stack. Till we found that no character in the stack has smaller ord(), then we can push the current into stack
        - Ex. stack has [c,a,f,g], current char is e
            - ord('g') > ord('e'), so we pop g --> stack become [c, a, f]
            - ord('f') > ord('e'), so again we pop f --> stack become [c, a]
            - ord('a') < ord('e'), so we push the e into stack --> stack become [c, a, e]
        :type s: str
        :rtype: str
        """
        import collections
        count = collections.Counter(s)
        added = [False for _ in range(26)]
        stack = []
        for character in s:
            count[character] -= 1 # What if count[char] become less than 0..? Will never happen since count is the counter of character in the string
            if added[ord(character) - ord('a')]:
                continue
            while stack and ord(stack[-1]) > ord(character) and count[stack[-1]] > 0:
                # only replace the character in the stack in these conditions:
                # 1. stack is not empty
                # 2. ord(curr) < ord(stack[-1]
                # 3. count[stack[-1]] > 0 (we need to make sure we have enought characters to add it back later)
                added[ord(stack.pop()) - ord('a')] = False
            stack.append(character)
            added[ord(character) - ord('a')] = True
        return ''.join(stack)

s = "123"
print Solution().removeDuplicateLetters(s)


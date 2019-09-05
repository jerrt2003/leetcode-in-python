# -*- coding: utf-8 -*-
import hash2
class Solution(object):
    def getHint(self, secret, guess):
        """
        :type secret: str
        :type guess: str
        :rtype: str
        """
        secret_count = hash2.Counter(secret)
        guess_count = hash2.Counter(guess)
        A, B = 0, 0
        for i in range(len(guess)):
            if secret[i] == guess[i]:
                A += 1
                guess_count[guess[i]] -= 1
                secret_count[guess[i]] -= 1
            elif guess[i] not in secret_count:
                guess_count[guess[i]] = 0
        for key, value in guess_count.items():
            B += min(secret_count[key], value)
        return str(str(A) + 'A' + str(B) + 'B')





secret = "1122"
guess = "1222"

print Solution().getHint(secret,guess)
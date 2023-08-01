class Solution:
    def validWordAbbreviation(self, word: str, abbr: str) -> bool:
        i, j = 0, 0
        while i < len(word) and j < len(abbr):
            if abbr[j].isdigit():
                if abbr[j] == "0":
                    return False
                count = 0
                while j < len(abbr) and abbr[j].isdigit():
                    count = 10 * count + int(abbr[j])
                    j += 1
                i += count
            else:
                if word[i] != abbr[j]:
                    return False
                i += 1
                j += 1
        return i == len(word) and j == len(abbr)

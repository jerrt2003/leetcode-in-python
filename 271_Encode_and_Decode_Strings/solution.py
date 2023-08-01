from typing import List


class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string."""
        ret = ""
        for word in strs:
            # 編碼格式："字串長度/字串"
            ret += str(len(word)) + "/" + word

        return ret

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings."""
        ret = []
        # i 為目前的 index，start 為目前字串的起始 index
        i = 0
        start = 0
        while i < len(s):
            if s[i] == "/":
                # 每當遇到 "/" 時，就代表從 start 到 i 為字串長度
                word_len = int(s[start:i])
                word = s[i + 1 : (i + 1) + word_len]
                ret.append(word)

                # 更新 i 和 start
                i += word_len + 1
                start = i
            else:
                i += 1

        return ret


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))

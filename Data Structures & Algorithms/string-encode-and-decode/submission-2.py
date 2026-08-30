class Solution:
    def encode(self, strs: List[str]) -> str:
        words = ""
        for n in strs:
            words += f"{len(n)}#{n}"
        return words

    def decode(self, s: str) -> List[str]:
        if s == "":
            return []

        decoded = []
        i = 0
        while i < len(s):
            j = i

            while s[j] != "#":
                j += 1

            length = int(s[i:j])
            start = j + 1
            word = s[start : start + length]
            decoded.append(word)
            i = start + length
        return decoded

class Solution:
    def isValid(self, s: str) -> bool:
        seen = []
        pairs = {
            ")": "(",
            "]": "[",
            "}": "{"
        }
        for n in s:
            if n in "([{":
                seen.append(n)
            else:
                if not seen:
                    return False
                if seen[-1] != pairs[n]:
                    return False
                seen.pop()
        return not seen

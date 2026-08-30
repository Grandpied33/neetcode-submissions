class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        seen = set()
        best = 0
        left = 0

        for i, n in enumerate(s):
            while n in seen:
                seen.remove(s[left])
                left += 1

            seen.add(n)
            best = max(best, len(seen))

        return best
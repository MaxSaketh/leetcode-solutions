# Last updated: 31/07/2026, 21:34:32
class Solution:
    def firstUniqChar(self, s: str) -> int:
        for ch in s:
            if s.count(ch) == 1:
                return s.index(ch)
        return -1


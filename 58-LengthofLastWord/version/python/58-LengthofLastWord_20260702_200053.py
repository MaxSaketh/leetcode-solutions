# Last updated: 02/07/2026, 20:00:53
1class Solution:
2    def lengthOfLastWord(self, s: str) -> int:
3        return len(s.split()[-1])
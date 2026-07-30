# Last updated: 30/07/2026, 20:16:06
1class Solution:
2    def truncateSentence(self, s: str, k: int) -> str:
3        s = s.split(" ")
4        return " ".join(s[:k])
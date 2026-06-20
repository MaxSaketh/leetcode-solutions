# Last updated: 20/06/2026, 19:46:37
1class Solution:
2    def reversePrefix(self, s: str, k: int) -> str:
3        return (s[:k])[::-1]+s[k:]
# Last updated: 23/06/2026, 18:53:37
1class Solution:
2    def strStr(self, haystack: str, needle: str) -> int:
3        for i in range(len(haystack)):
4            if haystack[i:i+len(needle)] == needle:
5                return i
6        return -1
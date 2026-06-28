# Last updated: 28/06/2026, 18:58:41
1#a = 97
2class Solution:
3    def reverseDegree(self, s: str) -> int:
4        ans = 0
5        for i in range(len(s)):
6            ans += (i + 1) * (26 - ord(s[i]) + 97)
7        return ans
8
# Last updated: 30/07/2026, 20:34:43
1class Solution:
2    def prefixCount(self, words: List[str], pref: str) -> int:
3        count = 0
4        l = len(pref)
5        for i in words:
6            if i[:l] == pref:
7                count += 1
8        return count
9
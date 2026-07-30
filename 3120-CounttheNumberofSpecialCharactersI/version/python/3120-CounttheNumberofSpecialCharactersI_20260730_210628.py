# Last updated: 30/07/2026, 21:06:28
1class Solution:
2    def numberOfSpecialChars(self, word: str) -> int:
3        x = []
4        for i in word:
5            if i.islower() and i.upper() in word and i not in x:
6                x.append(i)
7        return len(x)
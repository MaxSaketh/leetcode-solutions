# Last updated: 04/08/2026, 20:55:48
1class Solution:
2    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
3        c = 0
4
5        for i in words:
6            x = []
7            for j in allowed:
8                x.append(i.count(j))
9            if sum(x) == len(i):
10                c += 1
11                
12        return (c)
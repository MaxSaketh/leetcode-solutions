# Last updated: 25/06/2026, 19:25:58
# for loop method
1class Solution:
2    def defangIPaddr(self, address: str) -> str:
3        x = ""
4        for i in address:
5            if i != '.':
6                x += i
7                continue
8            x += '[.]'
9        return x
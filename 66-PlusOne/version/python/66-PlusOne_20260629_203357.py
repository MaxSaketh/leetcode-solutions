# Last updated: 29/06/2026, 20:33:57
1class Solution:
2    def plusOne(self, digits: List[int]) -> List[int]:
3        x = []
4        s = 0
5        for i in digits:
6            s = (s*10) + i
7        s += 1
8        for j in str(s):
9            x.append(int(j))
10        return x
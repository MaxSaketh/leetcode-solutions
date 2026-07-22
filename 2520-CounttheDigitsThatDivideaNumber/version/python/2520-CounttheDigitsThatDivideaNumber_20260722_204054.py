# Last updated: 22/07/2026, 20:40:54
1class Solution:
2    def countDigits(self, num: int) -> int:
3        c = 0
4        d = [int(i) for i in str(num)]
5        for j in d:
6            if num % j == 0:
7                c += 1
8        return c
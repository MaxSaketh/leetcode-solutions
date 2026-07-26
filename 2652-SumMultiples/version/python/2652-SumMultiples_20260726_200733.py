# Last updated: 26/07/2026, 20:07:33
1class Solution:
2    def sumOfMultiples(self, n: int) -> int:
3        s = 0
4        for i in range(1,n+1):
5            if i % 3 == 0 or i % 5 == 0 or i % 7 == 0:
6                s += i
7        return s
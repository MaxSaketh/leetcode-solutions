# Last updated: 20/07/2026, 20:46:06
1class Solution:
2    def smallestEvenMultiple(self, n: int) -> int:
3        for i in range(1,(2*n)+1):
4            if i % 2 == 0 and i % n == 0:
5                return i
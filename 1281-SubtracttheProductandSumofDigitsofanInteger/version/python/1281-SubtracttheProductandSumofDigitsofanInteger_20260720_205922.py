# Last updated: 20/07/2026, 20:59:22
1class Solution:
2    def subtractProductAndSum(self, n: int) -> int:
3        x = [int(i) for i in str(n)]
4        s = sum(x)
5        p = 1
6        for i in x:
7            p *= i
8        return p - s
9
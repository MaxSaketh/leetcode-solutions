# Last updated: 20/07/2026, 20:49:51
1class Solution:
2    def xorOperation(self, n: int, start: int) -> int:
3        x = 0
4        for i in range(n):
5            x ^= (start + 2 * i)
6        return x
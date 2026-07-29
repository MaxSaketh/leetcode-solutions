# Last updated: 29/07/2026, 19:57:20
1class Solution:
2    def reverseBits(self, n: int) -> int:
3        x = f"{n:032b}"[::-1]
4        return int(x, 2)
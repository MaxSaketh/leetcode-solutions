# Last updated: 29/07/2026, 20:00:32
1class Solution:
2    def hammingWeight(self, n: int) -> int:
3        return n.bit_count()
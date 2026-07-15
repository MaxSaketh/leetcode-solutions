# Last updated: 15/07/2026, 16:35:25
1import numpy as np 
2class Solution:
3    def gcdOfOddEvenSums(self, n: int) -> int:
4        sumE = n * (n + 1)
5        sumO = n * n
6        gcd = int(np.gcd(sumE, sumO))
7        return gcd
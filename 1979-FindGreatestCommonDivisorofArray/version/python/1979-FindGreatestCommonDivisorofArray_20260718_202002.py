# Last updated: 18/07/2026, 20:20:02
1import numpy as np
2class Solution:
3    def findGCD(self, nums: List[int]) -> int:
4        return int(np.gcd(max(nums), min(nums)))
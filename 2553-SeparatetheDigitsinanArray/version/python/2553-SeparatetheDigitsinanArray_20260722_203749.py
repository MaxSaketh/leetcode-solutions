# Last updated: 22/07/2026, 20:37:49
1class Solution:
2    def separateDigits(self, nums: List[int]) -> List[int]:
3        n = []
4        for i in nums:
5            n.extend([int(x) for x in str(i)])
6        return n
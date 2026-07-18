# Last updated: 18/07/2026, 20:26:34
1class Solution:
2    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
3        l = []
4
5        for i in nums:
6            if nums.count(i) > 1 and i not in l:
7                l.append(i)
8
9        return l
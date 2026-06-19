# Last updated: 19/06/2026, 18:54:25
1class Solution:
2    def twoSum(self, nums: List[int], target: int) -> List[int]:
3        for indi, i in enumerate(nums):
4            for indj, j in enumerate(nums):
5                if i + j == target and indi != indj:
6                    return [indi, indj]
7
8                    
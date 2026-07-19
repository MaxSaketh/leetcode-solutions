# Last updated: 19/07/2026, 18:54:49
1class Solution:
2    def majorityElement(self, nums: List[int]) -> int:
3        v = list(set(nums))
4        for i in v:
5            if nums.count(i) > len(nums)/2:
6                return i
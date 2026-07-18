# Last updated: 18/07/2026, 20:33:11
1class Solution:
2    def runningSum(self, nums: List[int]) -> List[int]:
3        s = []
4        for x in range(len(nums)):
5            s.append(sum(nums[0:x+1]))
6        return s
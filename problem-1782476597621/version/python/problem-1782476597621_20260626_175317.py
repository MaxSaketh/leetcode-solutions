# Last updated: 26/06/2026, 17:53:17
1class Solution:
2    def leftRightDifference(self, nums: List[int]) -> List[int]:
3        ans = []
4
5        for i in range(len(nums)):
6            x = sum(nums[:i])
7            y = sum(nums[i+1:])
8            ans.append(abs(x-y))
9        return ans
10        
11
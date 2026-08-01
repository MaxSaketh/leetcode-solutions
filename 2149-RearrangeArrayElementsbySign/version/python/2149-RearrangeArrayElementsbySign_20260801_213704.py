# Last updated: 01/08/2026, 21:37:04
1class Solution:
2    def rearrangeArray(self, nums: list[int]) -> list[int]:
3        result = [0] * len(nums)
4        pos_idx = 0
5        neg_idx = 1
6        
7        for num in nums:
8            if num > 0:
9                result[pos_idx] = num
10                pos_idx += 2
11            else:
12                result[neg_idx] = num
13                neg_idx += 2
14                
15        return result
16
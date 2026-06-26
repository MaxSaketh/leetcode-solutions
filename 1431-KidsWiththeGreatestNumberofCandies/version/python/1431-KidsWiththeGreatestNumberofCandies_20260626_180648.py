# Last updated: 26/06/2026, 18:06:48
1class Solution:
2    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
3        ans = []
4        for i in candies:
5            x = i + extraCandies
6            if x >= max(candies):
7                ans.append(True)
8            else:
9                ans.append(False)
10        return ans
11
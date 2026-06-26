# Last updated: 26/06/2026, 18:11:41
1class Solution:
2    def maximumWealth(self, accounts: List[List[int]]) -> int:
3        max = 0
4        for i in accounts:
5            x = sum(i)
6            if x > max:
7                max = x
8        return max
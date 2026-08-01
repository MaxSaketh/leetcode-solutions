# Last updated: 01/08/2026, 21:23:40
1class Solution:
2    def countDigitOccurrences(self, nums: list[int], digit: int) -> int:
3        c = 0
4        for i in nums:
5            x = str(i)
6            c += x.count(str(digit))
7        
8        return c
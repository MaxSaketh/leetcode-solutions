# Last updated: 19/06/2026, 19:06:52
1class Solution:
2    def isPalindrome(self, x: int) -> bool:
3        og = x
4        pal = 0
5        while x > 0:
6            l = x % 10
7            pal = pal*10 + l
8            x = x // 10
9        return (True if og == pal else False)
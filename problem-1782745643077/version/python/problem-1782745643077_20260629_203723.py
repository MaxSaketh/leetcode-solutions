# Last updated: 29/06/2026, 20:37:23
1class Solution:
2    def mySqrt(self, x: int) -> int:
3        if x < 2:
4            return x
5            
6        l, r = 2, x // 2
7        
8        while l <= r:
9            p = (l + r) // 2
10            num = p * p
11            
12            if num > x:
13                r = p - 1
14            elif num < x:
15                l = p + 1
16            else:
17                return p
18                
19        return r
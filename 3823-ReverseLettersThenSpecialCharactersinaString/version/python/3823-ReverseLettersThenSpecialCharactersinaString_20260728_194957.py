# Last updated: 28/07/2026, 19:49:57
1class Solution:
2    def reverseByType(self, s: str) -> str:
3        letters = [char for char in s if char.islower()]
4        specials = [char for char in s if not char.islower()]
5        
6        res = []
7        
8        for char in s:
9            if char.islower():
10                res.append(letters.pop())
11            else:
12                res.append(specials.pop())
13                
14        return "".join(res)
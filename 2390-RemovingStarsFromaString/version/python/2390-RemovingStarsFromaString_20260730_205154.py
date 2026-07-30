# Last updated: 30/07/2026, 20:51:54
1class Solution:
2    def removeStars(self, s: str) -> str:
3        ans = []
4        for c in s:
5            if c == '*':
6                ans.pop()  
7            else:
8                ans.append(c)  
9        return "".join(ans)
10